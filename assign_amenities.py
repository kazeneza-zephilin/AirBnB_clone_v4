#!/usr/bin/env python3
"""
Script to assign some amenities to places for testing search functionality
"""
import json
import random

def assign_amenities():
    # Read the current data
    with open('dev/file.json', 'r') as f:
        data = json.load(f)
    
    # Get all amenity IDs
    amenity_ids = [key.split('.')[1] for key in data.keys() if key.startswith('Amenity.')]
    print(f"Found {len(amenity_ids)} amenities")
    
    # Get all places
    place_keys = [key for key in data.keys() if key.startswith('Place.')]
    print(f"Found {len(place_keys)} places")
    
    # Assign 2-5 random amenities to each place
    for place_key in place_keys:
        place_data = data[place_key]
        num_amenities = random.randint(2, 5)
        selected_amenities = random.sample(amenity_ids, num_amenities)
        place_data['amenity_ids'] = selected_amenities
        print(f"Assigned {num_amenities} amenities to {place_data['name']}")
    
    # Save the updated data
    with open('dev/file.json', 'w') as f:
        json.dump(data, f)
    
    print("Amenities assigned successfully!")

if __name__ == "__main__":
    assign_amenities()
