import json
import sys

def round_coordinates(coords, precision=5):
    """
    Recursively round coordinates to specified precision.
    Handles nested coordinate arrays for different geometry types.
    """
    if isinstance(coords[0], list):
        return [round_coordinates(coord, precision) for coord in coords]
    else:
        # Base case: we have a coordinate pair [lon, lat]
        return [round(coord, precision) for coord in coords]

def filter_and_simplify_counties(input_file, output_file, target_counties, precision=5):
    """
    Read GeoJSON file, filter for specific counties, and round coordinates.
    
    Args:
        input_file: Path to input GeoJSON file
        output_file: Path to output GeoJSON file
        target_counties: List of county names to extract
        precision: Number of decimal places for coordinates (default: 5)
    """
    # Read the input GeoJSON file
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    # Filter features for target counties
    filtered_features = []
    
    for feature in data['features']:
        properties = feature['properties']
        
        # Check multiple possible property names for county name
        county_name = (
            properties.get('NAME_TAG') or 
            properties.get('NAME_EN') or 
            properties.get('name') or 
            properties.get('COUNTY') or 
            ''
        )
        
        # Check if this county matches any of our targets
        for target in target_counties:
            if target.lower() in county_name.lower():
                # Round coordinates
                if feature['geometry']['type'] == 'Polygon':
                    feature['geometry']['coordinates'] = round_coordinates(
                        feature['geometry']['coordinates'], 
                        precision
                    )
                elif feature['geometry']['type'] == 'MultiPolygon':
                    feature['geometry']['coordinates'] = round_coordinates(
                        feature['geometry']['coordinates'], 
                        precision
                    )
                
                filtered_features.append(feature)
                print(f"Found and processed: {county_name}")
                break
    
    # Create output GeoJSON structure
    output_data = {
        "type": "FeatureCollection",
        "features": filtered_features
    }
    
    # Write to output file
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, indent=2, ensure_ascii=False)
    
    print(f"\nProcessed {len(filtered_features)} counties")
    print(f"Output written to: {output_file}")
    
    return output_data

def main():
    # Define the four target counties
    target_counties = ['Antrim', 'Down', 'Donegal', 'Tyrone']
    
    # File paths
    input_file = 'counties.geojson'
    output_file = 'mccreary_counties.geojson'
    
    # Process the file
    try:
        result = filter_and_simplify_counties(
            input_file, 
            output_file, 
            target_counties, 
            precision=5
        )
        
        print("\n" + "="*50)
        print("SUCCESS!")
        print("="*50)
        print(f"\nExtracted counties:")
        for feature in result['features']:
            props = feature['properties']
            county_name = props.get('NAME_TAG') or props.get('NAME_EN') or 'Unknown'
            print(f"  - {county_name}")
        
    except FileNotFoundError:
        print(f"Error: Could not find '{input_file}'")
        print("Please make sure the file is in the same directory as this script.")
        sys.exit(1)
    except json.JSONDecodeError:
        print(f"Error: '{input_file}' is not a valid JSON file")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
