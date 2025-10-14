# Ancestor Locations Interactive Map

This interactive map visualization shows the birth and death locations of George Boal McCreary's ancestors across Pennsylvania and North Carolina.

## Application

[Launch Interactive Map](./main.html){ .md-button .md-button--primary }

## Overview

The map displays **33 locations** across Pennsylvania and North Carolina where ancestors of George Boal McCreary were born or died during the 1700s-1900s. The visualization helps understand the migration patterns and settlement locations of the McCreary, Bost, Boal, and related families.

### Features

- **Interactive Markers**: Click on any location to see detailed information about people and events
- **Color-Coded Markers**:
    - Green: Birth events only
    - Red: Death events only
    - Orange: Both birth and death events
- **Filters**: Filter locations by state (Pennsylvania or North Carolina) and event type (births/deaths)
- **Statistics**: Real-time counts of locations and events based on current filters
- **Marker Clustering**: Automatic grouping of nearby locations at higher zoom levels

### Geographic Distribution

**Pennsylvania Locations (24)**:
- Major counties: Beaver, Westmoreland, Centre, Lancaster, Venango, Armstrong
- Key towns: Baden, Greensburg, Leechburg, Greenville, Boalsburg

**North Carolina Locations (9)**:
- Major counties: Iredell, Mecklenburg, Rowan, Cabarrus, Craven
- Key towns: Statesville, New Bern, Conover

## Technical Details

### Data Source

The location data is derived from the genealogical records in [Ancestors of George Boal McCreary](../../content/02-family-history-and-genealogy/ancestors-of-george-boal-mccreary.md).

### Data Format

The visualization uses GeoJSON format with the following structure:

```json
{
  "type": "Feature",
  "geometry": {
    "type": "Point",
    "coordinates": [longitude, latitude]
  },
  "properties": {
    "name": "Location Name, County, State",
    "state": "State Name",
    "events": [
      {
        "person": "Person Name",
        "eventType": "birth|death",
        "date": "YYYY-MM-DD",
        "description": "Event description"
      }
    ]
  }
}
```

### Technology Stack

- **Leaflet.js**: Open-source mapping library
- **Leaflet.markercluster**: Marker clustering plugin
- **OpenStreetMap**: Map tile provider
- **GeoJSON**: Standardized geographic data format

### Files

- `main.html` - Interactive map application
- `pa-nc-places.json` - GeoJSON data file with location and event data
- `index.md` - This documentation

## Usage Instructions

1. **View All Locations**: The map initially shows all locations in both states
2. **Filter by State**: Use the dropdown to view only Pennsylvania or North Carolina
3. **Filter by Event Type**: Toggle checkboxes to show/hide births or deaths
4. **Explore Details**: Click any marker to see people and dates associated with that location
5. **Zoom and Pan**: Use mouse/touch to navigate the map

## Historical Context

The locations on this map represent the Pennsylvania and North Carolina branches of the family tree:

- **Pennsylvania Branch**: Primarily Scotch-Irish Presbyterians who settled in western Pennsylvania counties in the 1700s-1800s
- **North Carolina Branch**: The Bost family line with German roots (originally "Baust"), primarily in the Piedmont region

The map reveals the migration patterns from colonial settlements in Bucks and Lancaster counties westward to Westmoreland, Beaver, and Venango counties, as well as the North Carolina Piedmont settlements in Mecklenburg and Rowan counties.

## Future Enhancements

Possible additions to this visualization:

- Timeline slider to see locations chronologically
- Migration path lines connecting related locations
- Photos or historical context for each location
- Integration with additional family branches
- Export functionality for filtered data
- Mobile-responsive improvements

## Related Resources

- [Ancestors of George Boal McCreary](../../content/02-family-history-and-genealogy/ancestors-of-george-boal-mccreary.md) - Source genealogical data
- [Family History & Genealogy](../../content/02-family-history-and-genealogy/index.md) - Main genealogy section
- [Geography & Settlement Patterns](../../content/03-geography-settlement-patterns/index.md) - Historical migration context

---

*This interactive map was created to visualize the geographic distribution of the McCreary family ancestors across Pennsylvania and North Carolina during the 18th and 19th centuries.*
