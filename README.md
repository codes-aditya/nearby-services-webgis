# Nearby Services WebGIS (Pune)

A web map that finds hospitals, pharmacies, police stations, ATMs,
schools, fuel stations and parks near any location in Pune.

## Technology
- PostgreSQL [version] with PostGIS [version]
- GeoServer [version]
- Leaflet 1.9.4 (HTML, CSS, JavaScript)
- Data: OpenStreetMap via the Overpass API

## Folders
- frontend/    the web page (index.html, Leaflet files)
- database/    data loader, database backup and SQL queries
- geoserver/   GeoServer settings and setup notes
- screenshots/ pictures of the working application
- report.pdf   project report

## How to run
1. Install PostgreSQL, PostGIS and GeoServer.
2. Create a database named gis and run: CREATE EXTENSION postgis;
3. Restore the data: psql -U postgres -d gis -f database/poi_dump.sql
4. Start GeoServer. Create workspace "services" and a PostGIS store "gis_db".
5. Publish the table "poi" and create the SQL view "nearby_pois"
   (see geoserver/geoserver_setup.md and database/nearby_pois_view.sql).
6. Copy the files in frontend/ to C:\ProgramData\GeoServer\www
7. Open http://localhost:8080/geoserver/www/index.html

## Features
- Location by map click, latitude/longitude or browser geolocation
- Category and subcategory filters
- Radius search, nearest-N search, or both
- Results sorted by distance, linked to map markers
- Details panel and popup for each service
- PostGIS spatial query (EPSG:4326, distance in metres)
- GeoServer WMS and WFS layers
- Error messages for denied location, invalid input and no results

## Limits
Data covers central Pune only. Subcategories depend on OpenStreetMap tags.