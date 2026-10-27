import re, requests, psycopg2

DB = dict(host="localhost", port=5432, dbname="nearby_services",
          user="postgres", password="K16@sweety")

# south, west, north, east  (this box covers Pune; change it for another area)
BBOX = "18.40,73.72,18.67,74.00"

QUERY = f"""
[out:json][timeout:180];
(
  nwr["amenity"~"^(hospital|clinic|pharmacy|police|atm|school|fuel)$"]({BBOX});
  nwr["leisure"="park"]({BBOX});
);
out center tags;
"""

import time

HEADERS = {
    "User-Agent": "NearbyServicesGISLab/1.0 (student project; contact: k16aditya@gmail.com)",
    "Accept": "application/json",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

SERVERS = [
    "https://overpass-api.de/api/interpreter",
    "https://overpass.private.coffee/api/interpreter",
    "https://overpass.kumi.systems/api/interpreter",
]

elements = None
for attempt in range(1, 4):                      # up to 3 rounds
    for url in SERVERS:
        try:
            print(f"Round {attempt}: downloading from {url} (1-3 minutes)...")
            r = requests.post(url, data={"data": QUERY}, headers=HEADERS, timeout=300)
            r.raise_for_status()
            elements = r.json()["elements"]
            break
        except Exception as ex:
            print("Failed:", ex)
            time.sleep(5)
    if elements is not None:
        break
    print("All servers failed. Waiting 60 seconds before retrying...")
    time.sleep(60)

if elements is None:
    raise SystemExit("Could not download data. Try again in 10-15 minutes.")
print(len(elements), "features downloaded")

def clean(v):
    return re.sub(r"[^a-z0-9_ ]", "_", v.lower().split(";")[0].strip())

conn = psycopg2.connect(**DB)
cur = conn.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS poi (
  id serial PRIMARY KEY,
  osm_id text UNIQUE,
  name text, category text, subcategory text,
  address text, phone text, website text, opening_hours text,
  geom geometry(Point,4326)
);""")

count = 0
for e in elements:
    tags = e.get("tags", {})
    lat = e.get("lat");  lon = e.get("lon")
    if lat is None:
        c = e.get("center") or {}
        lat, lon = c.get("lat"), c.get("lon")
    if lat is None or lon is None:
        continue
    category = tags.get("amenity") or ("park" if tags.get("leisure") == "park" else None)
    if not category:
        continue
    name = tags.get("name") or tags.get("name:en") or f"Unnamed {category}"
    sub = tags.get("healthcare:speciality") or tags.get("operator:type") or tags.get("brand") or "general"
    address = " ".join(filter(None, [tags.get("addr:housenumber"),
                                     tags.get("addr:street"), tags.get("addr:suburb")]))
    cur.execute("""
      INSERT INTO poi (osm_id,name,category,subcategory,address,phone,website,opening_hours,geom)
      VALUES (%s,%s,%s,%s,%s,%s,%s,%s, ST_SetSRID(ST_MakePoint(%s,%s),4326))
      ON CONFLICT (osm_id) DO NOTHING""",
      (f"{e['type']}/{e['id']}", name, category, clean(sub), address,
       tags.get("phone"), tags.get("website"), tags.get("opening_hours"), lon, lat))
    count += 1

cur.execute("CREATE INDEX IF NOT EXISTS poi_geom_gix ON poi USING GIST (geom)")
cur.execute("CREATE INDEX IF NOT EXISTS poi_geog_gix ON poi USING GIST ((geom::geography))")
cur.execute("CREATE INDEX IF NOT EXISTS poi_cat_idx ON poi (category, subcategory)")
conn.commit()
cur.execute("ANALYZE poi")
conn.commit()
print("Inserted", count, "places. Done.")