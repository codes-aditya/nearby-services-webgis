-- GeoServer SQL view "nearby_pois"
-- Parameters: lat, lng, radius (metres), n, cats (separator |), sub

SELECT id, name, category, subcategory, address, phone, website, opening_hours,
  ST_Y(geom) AS y_lat,
  ST_X(geom) AS x_lng,
  ST_Distance(geom::geography,
    ST_SetSRID(ST_MakePoint(%lng%,%lat%),4326)::geography) AS dist_m,
  geom
FROM poi
WHERE category = ANY(string_to_array('%cats%','|'))
  AND ('%sub%' = 'all' OR subcategory = '%sub%')
  AND ST_DWithin(geom::geography,
    ST_SetSRID(ST_MakePoint(%lng%,%lat%),4326)::geography, %radius%)
ORDER BY dist_m
LIMIT %n%