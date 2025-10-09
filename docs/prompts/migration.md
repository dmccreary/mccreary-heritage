# Migration Map

!!! prompt
    Please generate a web application that displays a map of the world including Scotland, Ireland and North America.  Add a "Show Migration" button in the control area below the map that the user can click to see the migration from Scotland to Ireland and then to the Americas.  Use the leaflet JavaScript library and include open maps as the background below the arrows.

## Claude Sonnet Response

I'll create an interactive map application showing the McCreary family migration patterns using Leaflet.js with OpenStreetMap tiles.I've created an interactive migration map for the McCreary family heritage. Here are the key features:

**Map Features:**

- Uses Leaflet.js with OpenStreetMap tiles as the background
- Shows five key locations: Lowland Scotland, Ulster (Ireland), Philadelphia, Cumberland Valley (PA), and Shenandoah Valley (VA)
- Color-coded markers distinguish different phases: Scotland (blue), Ulster (green), North America (red)

**Interactive Controls:**

- **Show Migration** button animates the migration routes in sequence:
  1. Scotland → Ulster (1610s plantation)
  2. Ulster → Philadelphia (1717-1775 emigration)
  3. Philadelphia → Cumberland Valley → Shenandoah Valley (frontier settlement)
- **Reset Map** button clears the animation and returns to the initial view

**Visual Design:**

- Animated dashed lines show migration paths
- Circular markers with popup information for each location
- Legend explaining the color coding
- Migration timeline information panel that appears when showing the migration
- Consistent styling matching the McCreary heritage site theme

The map automatically adjusts to show all locations when the migration is displayed, and users can click on any marker to see more details about that location's significance in McCreary family history.