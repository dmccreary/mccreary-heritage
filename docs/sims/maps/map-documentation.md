# McCreary Settlement Counties Map - Technical Documentation

## Overview

This interactive web map displays the four primary Ulster counties where McCreary families settled during the Ulster Plantation period (1610-1718): Antrim, Down, Donegal, and Tyrone. The map uses the Leaflet JavaScript library to render precise county boundaries loaded from a GeoJSON file.

## Files Required

### 1. main.html
The main HTML file containing the complete web application.

### 2. mccreary-counties.geojson
A GeoJSON file containing the precise boundary coordinates for the four counties. This file must be in the same directory as the HTML file.

**Format:** Standard GeoJSON FeatureCollection with Polygon or MultiPolygon geometries.

**Expected Properties:** The features should contain at least one of these property names for the county name:
- `NAME_TAG`
- `NAME_EN`
- `name`
- `COUNTY`

## Configuration Parameters

### Map Initialization

Located in the `loadCountyBoundaries()` function:

```javascript
map = L.map('map').setView([54.7, -7.0], 8);
```

**Parameters:**
- **Center coordinates:** `[54.7, -7.0]` (latitude, longitude)
  - Current: Centered on Northern Ireland
  - Modify: Change to any lat/lng to center the map elsewhere
  
- **Initial zoom level:** `8`
  - Range: 1-18 (1 = world view, 18 = street level)
  - Current: Shows all four counties comfortably
  - Recommended range: 7-10 for regional view

### Zoom Constraints

```javascript
maxZoom: 18,
minZoom: 7
```

**Parameters:**
- **maxZoom:** `18` - Maximum zoom in level (street detail)
- **minZoom:** `7` - Minimum zoom out level (prevents zooming too far out)

### Map Tile Provider

```javascript
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
    maxZoom: 18,
    minZoom: 7
}).addTo(map);
```

**Alternative Tile Providers:**

You can replace OpenStreetMap with other providers by changing the URL:

- **CartoDB Positron (light, minimal):**
  ```javascript
  'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png'
  ```

- **CartoDB Dark Matter (dark theme):**
  ```javascript
  'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png'
  ```

- **Stamen Terrain (topographic):**
  ```javascript
  'https://stamen-tiles-{s}.a.ssl.fastly.net/terrain/{z}/{x}/{y}{r}.png'
  ```

## Style Configuration

### County Boundary Styles

Located in the `style()` function:

```javascript
function style(feature) {
    return {
        fillColor: '#3b82f6',
        fillOpacity: 0.2,
        color: '#1e3a8a',
        weight: 3,
        opacity: 0.9
    };
}
```

**Parameters:**
- **fillColor:** `'#3b82f6'` - Interior fill color (blue)
  - Format: Hex color code or CSS color name
  
- **fillOpacity:** `0.2` - Transparency of fill (0.0 = transparent, 1.0 = solid)
  - Range: 0.0 to 1.0
  
- **color:** `'#1e3a8a'` - Border line color (dark blue)
  - Format: Hex color code or CSS color name
  
- **weight:** `3` - Border line thickness in pixels
  - Range: 1-10 (recommended)
  
- **opacity:** `0.9` - Border line transparency
  - Range: 0.0 to 1.0

### Hover/Highlight Styles

Located in the `highlightFeature()` function:

```javascript
layer.setStyle({
    weight: 5,
    color: '#1e40af',
    fillOpacity: 0.35
});
```

**Parameters:**
- **weight:** `5` - Border thickness when hovering (pixels)
- **color:** `'#1e40af'` - Border color when hovering (darker blue)
- **fillOpacity:** `0.35` - Fill transparency when hovering

### County Label Styles

Located in CSS `.county-label` class:

```css
.county-label {
    background: rgba(30, 58, 138, 0.85);
    color: white;
    padding: 8px 16px;
    border-radius: 6px;
    font-size: 1.3em;
    font-weight: 600;
    border: 2px solid white;
    box-shadow: 0 2px 8px rgba(0,0,0,0.3);
}
```

**Customizable Properties:**
- **background:** `rgba(30, 58, 138, 0.85)` - Label background color
  - Format: rgba(red, green, blue, alpha) where values are 0-255, alpha is 0-1
  
- **color:** `white` - Text color
  
- **padding:** `8px 16px` - Space inside label (vertical horizontal)
  
- **border-radius:** `6px` - Corner rounding
  
- **font-size:** `1.3em` - Text size (relative to base font)
  
- **font-weight:** `600` - Text boldness (100-900)
  
- **border:** `2px solid white` - Border width, style, and color

### Hover Label Effect

Located in CSS `.county-label-hover` class:

```css
.county-label-hover {
    background: rgba(30, 64, 175, 0.95);
    transform: scale(1.1);
    transition: all 0.2s ease;
}
```

**Parameters:**
- **transform: scale():** `1.1` - Size increase on hover (1.0 = normal, 1.1 = 10% larger)
- **transition:** `0.2s` - Animation duration in seconds

## County Descriptions

Located in the `countyDescriptions` object:

```javascript
const countyDescriptions = {
    'Antrim': 'Description text...',
    'Down': 'Description text...',
    'Donegal': 'Description text...',
    'Tyrone': 'Description text...'
};
```

**Customization:**
Edit the text strings to change the popup content that appears when clicking on a county.

## Header Customization

### Title and Subtitle

Located in the HTML header section:

```html
<h1>🗺️ McCreary Family Settlement Counties</h1>
<p>Primary Ulster Counties Where McCreary Families Settled (1610-1718)</p>
```

**Customization:**
- Change the emoji, title text, or subtitle as needed
- The emoji can be removed or replaced with any Unicode emoji

### Header Colors

Located in CSS `.header` class:

```css
background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
```

**Parameters:**
- **135deg:** Gradient angle (0-360 degrees)
- **#1e3a8a:** Start color (dark blue)
- **#3b82f6:** End color (light blue)

## Map Dimensions

Located in CSS `#map` style:

```css
#map {
    height: 700px;
}
```

**Parameters:**
- **height:** `700px` - Map height in pixels
  - Recommended range: 500-900px for desktop
  - Consider using responsive units (vh) for mobile: `height: 70vh;`

## Auto-Fitting to Counties

Located in `loadCountyBoundaries()` function:

```javascript
map.fitBounds(geojsonLayer.getBounds());
```

This automatically adjusts the map view to show all loaded counties optimally.

**Optional padding:** Add padding around the bounds:
```javascript
map.fitBounds(geojsonLayer.getBounds(), {padding: [50, 50]});
```

## Scale Control

Located at the end of `loadCountyBoundaries()`:

```javascript
L.control.scale({imperial: true, metric: true}).addTo(map);
```

**Parameters:**
- **imperial:** `true` - Show miles/feet
- **metric:** `true` - Show kilometers/meters
- Set either to `false` to hide that unit system

**Position options:**
```javascript
L.control.scale({
    imperial: true, 
    metric: true,
    position: 'bottomleft'  // or 'bottomright', 'topleft', 'topright'
}).addTo(map);
```

## Error Handling

The application includes error handling for:
- Missing GeoJSON file
- Invalid JSON format
- Empty feature collection
- Network errors

Error messages are displayed in a red box above the map with helpful guidance.

## Browser Compatibility

**Required:**
- Modern browser with JavaScript enabled
- ES6/ES2015 support (async/await)
- Fetch API support

**Tested on:**
- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+

## Dependencies

### Leaflet.js
- **Version:** 1.9.4
- **CDN:** cdnjs.cloudflare.com
- **License:** BSD-2-Clause

**Files loaded:**
- `leaflet.min.js` - JavaScript library
- `leaflet.min.css` - Styling

## Performance Considerations

### GeoJSON File Size
- Current implementation: 5 decimal places (~1 meter precision)
- Larger files (more precision) = slower loading
- Smaller files (less precision) = faster loading but less detail

**Optimization options:**
1. Reduce decimal places (4 = ~11m precision)
2. Use TopoJSON instead of GeoJSON (smaller file size)
3. Simplify geometries using tools like mapshaper.org

### Label Performance
- 4 permanent labels: minimal performance impact
- Adding more counties: consider lazy loading labels on zoom

## Customization Examples

### Example 1: Change to Dark Theme

```css
body {
    background: #1a1a2e;
}

.header {
    background: linear-gradient(135deg, #16213e 0%, #0f3460 100%);
}

.county-label {
    background: rgba(15, 52, 96, 0.9);
}
```

### Example 2: Adjust Initial View for Mobile

```javascript
// Detect mobile and adjust zoom
const isMobile = window.innerWidth < 768;
const zoomLevel = isMobile ? 7 : 8;
map = L.map('map').setView([54.7, -7.0], zoomLevel);
```

### Example 3: Add Click Coordinates Display

```javascript
map.on('click', function(e) {
    console.log('Clicked at: ' + e.latlng.toString());
});
```

## Troubleshooting

### Map not loading
1. Check browser console for errors (F12)
2. Verify `mccreary-counties.geojson` is in the correct directory
3. Ensure the GeoJSON file is valid JSON (use jsonlint.com)

### Counties not appearing
1. Check that GeoJSON has a "features" array
2. Verify coordinate format is [longitude, latitude] not [lat, lng]
3. Check that coordinates are in WGS84 (EPSG:4326)

### Labels not centered correctly
- The center is calculated from the bounding box, not the geometric centroid
- For irregular shapes, consider manually specifying label positions

## Future Enhancement Ideas

1. **Search functionality** - Find specific townlands or locations
2. **Historical overlays** - Show plantation boundaries or settlement patterns
3. **Timeline slider** - Display changes over different time periods
4. **Export features** - Download map as image or PDF
5. **Additional layers** - Churches, graveyards, historical sites
6. **Mobile optimization** - Touch-friendly controls and responsive design
7. **Print stylesheet** - Optimized view for printing
8. **Legend** - Visual key explaining map symbols and colors

## License and Credits

- Map data: © OpenStreetMap contributors
- Leaflet library: © Vladimir Agafonkin (BSD-2-Clause License)
- County boundaries: Ordnance Survey of Northern Ireland Open Data

## Support

For questions or issues with this map implementation, refer to:
- Leaflet documentation: https://leafletjs.com/reference.html
- GeoJSON specification: https://geojson.org/
- Leaflet tutorials: https://leafletjs.com/examples.html