# Nearby Services Finder WebGIS

A web-based Geographic Information System (WebGIS) application designed to help users locate nearby essential services using interactive maps, geolocation, and spatial queries.

The application integrates **Leaflet.js, GeoServer, PostgreSQL, and PostGIS** to visualize Points of Interest (POIs), perform distance-based searches, and identify nearby facilities.

## Project Overview

The Nearby Services Finder WebGIS allows users to search for nearby facilities such as hospitals, pharmacies, and other essential services.

Users can specify their location, select a service category, and search for facilities based on a distance radius or the nearest number of results.

The project demonstrates the integration of frontend web mapping with spatial databases and GIS web services.

## Key Features

- Interactive map visualization using Leaflet.js
- Browser-based user geolocation
- Search for nearby services by category
- Radius-based spatial search
- Nearest-N facility search
- Integration with GeoServer WMS and WFS services
- Spatial querying using PostgreSQL/PostGIS
- Display of service locations and distance-based results

## Technologies Used

| Technology | Purpose |
|---|---|
| HTML5 | Web application structure |
| CSS3 | User interface styling |
| JavaScript | Application functionality |
| Leaflet.js | Interactive web mapping |
| GeoServer | Publishing GIS web services |
| PostgreSQL | Spatial database management |
| PostGIS | Spatial queries and distance calculations |
| WMS | Rendering map layers |
| WFS | Retrieving geographic features |

## System Architecture

The application follows a three-layer WebGIS architecture.

**Frontend**

HTML, CSS, JavaScript, and Leaflet.js provide the interactive map, user controls, and search interface.

**GIS Server**

GeoServer publishes spatial data through WMS and WFS services and connects the frontend to the spatial database.

**Spatial Database**

PostgreSQL with PostGIS stores service locations and supports spatial operations such as radius filtering and nearest-neighbor searches.

### Data Flow

```text
User
  |
  v
Web Browser
(HTML + CSS + JavaScript)
  |
  v
Leaflet Interactive Map
  |
  v
GeoServer (WMS / WFS)
  |
  v
PostgreSQL + PostGIS
  |
  v
Spatial Queries
  |
  v
Nearby Service Results
  |
  v
Interactive Map Display
```

## Spatial Analysis

The application uses PostGIS spatial functions to identify services near a selected location.

### Radius-Based Search

`ST_DWithin()` identifies service locations within a specified distance from the user's location.

### Distance Calculation

`ST_Distance()` calculates the distance between the user and service locations.

### Nearest Facility Search

Distance-based sorting with `ORDER BY` and `LIMIT` can retrieve the nearest N facilities.

These operations demonstrate practical applications of spatial SQL in location-based services.

## Project Structure

```text
NearbyServices_WebGIS/
|
|-- index.html
|-- leaflet.css
|-- leaflet.js
|-- database/
|   |-- queries.sql
|   |-- nearby_pois_view.sql
|-- docs/
|   |-- geoserver_setup.md
|-- screenshots/
|   |-- dashboard.png
|-- README.md
```

*The structure above is a suggested organization. Actual files and directories may differ.*

## Installation and Setup

### 1. Prerequisites

Install and configure:

- PostgreSQL with PostGIS extension
- GeoServer
- A modern web browser
- A local web server or development environment

### 2. Configure the Spatial Database

Create a PostgreSQL database and enable the PostGIS extension.

```sql
CREATE EXTENSION IF NOT EXISTS postgis;
```

Import the Points of Interest dataset into a spatial table.

### 3. Configure GeoServer

1. Start GeoServer.
2. Create a workspace named `services`.
3. Connect GeoServer to the PostgreSQL/PostGIS database.
4. Publish the POI layer as `services:poi`.
5. Configure the SQL view layer `services:nearby_pois` if using parameterized spatial queries.
6. Enable the required WMS and WFS services.

### 4. Run the Application

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/nearby-services-webgis.git
```

Open the project folder in VS Code and run the frontend through a local development server.

Make sure GeoServer is running at the URL configured in `index.html`.

The development configuration uses:

```text
http://localhost:8080/geoserver
```

**Note:** The application requires a working GeoServer/PostGIS backend. Hosting the frontend on GitHub Pages alone will not make locally hosted GIS services publicly accessible.

## Screenshots

### WebGIS Dashboard

![Nearby Services Finder Dashboard](screenshots/dashboard.png)

## Applications

- Locating nearby healthcare facilities
- Identifying essential public services
- Location-based service discovery
- Spatial accessibility analysis
- GIS-based decision support
- Educational demonstrations of WebGIS and PostGIS

## Future Enhancements

- Road-network-based routing and travel-time analysis
- Additional service categories
- Mobile-responsive interface improvements
- Public cloud deployment
- Advanced spatial accessibility analysis
- Integration of real-time service information

## Author

**Aditya Singh**

M.Sc. Data Science & Spatial Analytics  
Symbiosis Institute of Geoinformatics, Pune

## Project Status

Academic WebGIS project demonstrating the integration of interactive web mapping, GIS web services, and spatial database queries.
