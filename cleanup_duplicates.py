#!/usr/bin/python3
"""
Script to remove duplicate states and amenities from the AirBnB clone database
This script keeps only one instance of each duplicate entry and removes the rest.
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

# Set environment variable for file storage
os.environ['HBNB_TYPE_STORAGE'] = 'file'

from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

# Force reload the storage to ensure we get the latest data
storage.reload()


def cleanup_duplicate_states():
    """Remove duplicate states, keeping only the first occurrence of each"""
    print("Cleaning up duplicate states...")
    
    all_states = storage.all('State')
    seen_names = {}
    states_to_delete = []
    
    for state in all_states.values():
        name = state.name
        if name in seen_names:
            # This is a duplicate - mark for deletion
            states_to_delete.append(state)
            print(f"  Marking duplicate state '{name}' for deletion (ID: {state.id})")
        else:
            # First occurrence - keep it
            seen_names[name] = state
            print(f"  Keeping state '{name}' (ID: {state.id})")
    
    # Delete duplicate states
    for state in states_to_delete:
        storage.delete(state)
    
    print(f"Deleted {len(states_to_delete)} duplicate states")
    return len(states_to_delete)


def cleanup_duplicate_amenities():
    """Remove duplicate amenities, keeping only the first occurrence of each"""
    print("Cleaning up duplicate amenities...")
    
    all_amenities = storage.all('Amenity')
    seen_names = {}
    amenities_to_delete = []
    
    for amenity in all_amenities.values():
        name = amenity.name
        if name in seen_names:
            # This is a duplicate - mark for deletion
            amenities_to_delete.append(amenity)
            print(f"  Marking duplicate amenity '{name}' for deletion (ID: {amenity.id})")
        else:
            # First occurrence - keep it
            seen_names[name] = amenity
            print(f"  Keeping amenity '{name}' (ID: {amenity.id})")
    
    # Delete duplicate amenities
    for amenity in amenities_to_delete:
        storage.delete(amenity)
    
    print(f"Deleted {len(amenities_to_delete)} duplicate amenities")
    return len(amenities_to_delete)


def cleanup_orphaned_cities():
    """Remove cities that reference deleted states"""
    print("Cleaning up orphaned cities...")
    
    all_cities = storage.all('City')
    all_states = storage.all('State')
    state_ids = set(state.id for state in all_states.values())
    
    cities_to_delete = []
    
    for city in all_cities.values():
        if city.state_id not in state_ids:
            cities_to_delete.append(city)
            print(f"  Marking orphaned city '{city.name}' for deletion (state_id: {city.state_id})")
    
    # Delete orphaned cities
    for city in cities_to_delete:
        storage.delete(city)
    
    print(f"Deleted {len(cities_to_delete)} orphaned cities")
    return len(cities_to_delete)


def update_place_amenities():
    """Update places to reference the remaining amenities"""
    print("Updating place amenity references...")
    
    all_places = storage.all(Place)
    all_amenities = storage.all(Amenity)
    
    # Create mapping from amenity name to ID for remaining amenities
    amenity_mapping = {amenity.name: amenity.id for amenity.id, amenity in all_amenities.items()}
    
    updated_places = 0
    
    for place in all_places.values():
        # Note: This is a simplified approach. In a real scenario, you'd need to 
        # check the place_amenity table and update references there.
        # For now, we'll just ensure places exist and can be found.
        if hasattr(place, 'amenity_ids') and place.amenity_ids:
            print(f"  Place '{place.name}' has amenities, checking references...")
        updated_places += 1
    
    print(f"Checked {updated_places} places for amenity references")
    return updated_places


def main():
    """Main function to clean up all duplicates"""
    print("Starting AirBnB Clone Duplicate Cleanup...")
    print("This will remove duplicate states and amenities, keeping only one of each.\n")
    
    # Count current data before cleanup
    all_states = storage.all('State')
    all_amenities = storage.all('Amenity')
    all_cities = storage.all('City')
    
    print(f"Before cleanup:")
    print(f"  States: {len(all_states)}")
    print(f"  Amenities: {len(all_amenities)}")
    print(f"  Cities: {len(all_cities)}")
    print()
    
    # Perform cleanup
    deleted_states = cleanup_duplicate_states()
    deleted_amenities = cleanup_duplicate_amenities()
    deleted_cities = cleanup_orphaned_cities()
    
    # Save changes
    storage.save()
    
    # Count data after cleanup
    all_states = storage.all('State')
    all_amenities = storage.all('Amenity')
    all_cities = storage.all('City')
    
    print(f"\nAfter cleanup:")
    print(f"  States: {len(all_states)}")
    print(f"  Amenities: {len(all_amenities)}")
    print(f"  Cities: {len(all_cities)}")
    print()
    
    print(f"Summary:")
    print(f"  Deleted {deleted_states} duplicate states")
    print(f"  Deleted {deleted_amenities} duplicate amenities")
    print(f"  Deleted {deleted_cities} orphaned cities")
    print(f"  Total items removed: {deleted_states + deleted_amenities + deleted_cities}")
    
    print("\nCleanup completed successfully!")


if __name__ == "__main__":
    main()
