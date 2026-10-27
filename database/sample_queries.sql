-- 1. Radius search: pharmacies within 2 km (distance in metres)
SELECT name, ROUND(ST_Distance(geom::geography,
       ST_SetSRID(ST_MakePoint(73.8553,18.5195),4326)::geography)::numeric) AS dist_m
FROM poi
WHERE category = 'pharmacy'
  AND ST_DWithin(geom::geography,
       ST_SetSRID(ST_MakePoint(73.8553,18.5195),4326)::geography, 2000)
ORDER BY dist_m;

-- 2. Nearest-N search: 5 nearest hospitals
SELECT name, ROUND(ST_Distance(geom::geography,
       ST_SetSRID(ST_MakePoint(73.8553,18.5195),4326)::geography)::numeric) AS dist_m
FROM poi
WHERE category = 'hospital'
ORDER BY geom::geography <-> ST_SetSRID(ST_MakePoint(73.8553,18.5195),4326)::geography
LIMIT 5;

-- 3. Count of services per category
SELECT category, COUNT(*) FROM poi GROUP BY category ORDER BY 2 DESC;

-- 4. Check the coordinate system (should show 4326)
SELECT Find_SRID('public','poi','geom');