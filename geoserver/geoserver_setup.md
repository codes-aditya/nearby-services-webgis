GeoServer setup

Version: http://localhost:8080/geoserver

1. Workspace
   Name: services
   Namespace URI: http://localhost/services

2. Data store (PostGIS)
   Name: gis_db
   Host: localhost   Port: 5432   Database: gis   Schema: public   User: postgres

3. Layer 1: services:poi
   A normal published table layer. Used as the WMS layer on the map.
   CRS: EPSG:4326
   Bounding box: 73.72, 18.40, 74.00, 18.67

4. Layer 2: services:nearby_pois
   A SQL view layer. It runs the PostGIS radius and nearest-N query.
   The SQL is in database/nearby_pois_view.sql

   Parameters and validation:
   lat      default 18.5204   ^-?[0-9]+(\.[0-9]+)?$
   lng      default 73.8567   ^-?[0-9]+(\.[0-9]+)?$
   radius   default 3000      ^[0-9]+$
   n        default 20        ^[0-9]+$
   cats     default hospital  ^[a-z_\|]+$
   sub      default all       ^[A-Za-z0-9_ ]+$

   Geometry column: geom, type Point, SRID 4326
   Identifier: id
   The validation rules stop SQL injection.

5. How the frontend calls it
   WFS GetFeature on services:nearby_pois with the viewparams parameter, for example:
   viewparams=lat:18.5204;lng:73.8567;radius:3000;n:10;cats:hospital|pharmacy;sub:all

6. Settings changed
   - Content Security Policy: allowed sources set to include tile.openstreetmap.org so map tiles load.
   - Static page hosted at C:\ProgramData\GeoServer\www