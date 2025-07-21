#!/usr/bin/python3
"""
Script to populate the AirBnB clone with comprehensive sample data
This demonstrates all functionality including:
- States and Cities
- Users (hosts and guests)
- Amenities
- Places with various configurations
- Reviews and ratings
"""

import sys
import os
sys.path.insert(0, os.path.abspath('.'))

from models import storage
from models.state import State
from models.city import City
from models.user import User
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


def create_states_and_cities():
    """Create states and their major cities"""
    print("Creating States and Cities...")
    
    # California
    california = State(name="California")
    california.save()
    
    sf = City(name="San Francisco", state_id=california.id)
    sf.save()
    
    la = City(name="Los Angeles", state_id=california.id)
    la.save()
    
    san_diego = City(name="San Diego", state_id=california.id)
    san_diego.save()
    
    # New York
    new_york = State(name="New York")
    new_york.save()
    
    nyc = City(name="New York City", state_id=new_york.id)
    nyc.save()
    
    buffalo = City(name="Buffalo", state_id=new_york.id)
    buffalo.save()
    
    # Florida
    florida = State(name="Florida")
    florida.save()
    
    miami = City(name="Miami", state_id=florida.id)
    miami.save()
    
    orlando = City(name="Orlando", state_id=florida.id)
    orlando.save()
    
    # Texas
    texas = State(name="Texas")
    texas.save()
    
    austin = City(name="Austin", state_id=texas.id)
    austin.save()
    
    houston = City(name="Houston", state_id=texas.id)
    houston.save()
    
    return {
        'states': [california, new_york, florida, texas],
        'cities': [sf, la, san_diego, nyc, buffalo, miami, orlando, austin, houston]
    }


def create_users():
    """Create sample users (hosts and guests)"""
    print("Creating Users...")
    
    users = []
    
    # Hosts
    host1 = User(
        email="john.host@example.com",
        password="hostpass123",
        first_name="John",
        last_name="Smith"
    )
    host1.save()
    users.append(host1)
    
    host2 = User(
        email="sarah.host@example.com", 
        password="hostpass456",
        first_name="Sarah",
        last_name="Johnson"
    )
    host2.save()
    users.append(host2)
    
    host3 = User(
        email="mike.host@example.com",
        password="hostpass789", 
        first_name="Mike",
        last_name="Davis"
    )
    host3.save()
    users.append(host3)
    
    # Guests
    guest1 = User(
        email="alice.guest@example.com",
        password="guestpass123",
        first_name="Alice",
        last_name="Wilson"
    )
    guest1.save()
    users.append(guest1)
    
    guest2 = User(
        email="bob.guest@example.com",
        password="guestpass456",
        first_name="Bob", 
        last_name="Brown"
    )
    guest2.save()
    users.append(guest2)
    
    guest3 = User(
        email="emma.guest@example.com",
        password="guestpass789",
        first_name="Emma",
        last_name="Taylor"
    )
    guest3.save()
    users.append(guest3)
    
    return {'hosts': users[:3], 'guests': users[3:], 'all': users}


def create_amenities():
    """Create various amenities"""
    print("Creating Amenities...")
    
    amenities_data = [
        "WiFi", "TV", "Kitchen", "Washer", "Dryer", "Air conditioning",
        "Heating", "Pool", "Gym", "Parking", "Hot tub", "Fireplace",
        "Balcony", "Garden", "Beach access", "Mountain view", "City view",
        "Pet friendly", "Smoking allowed", "Family friendly"
    ]
    
    amenities = []
    for amenity_name in amenities_data:
        amenity = Amenity(name=amenity_name)
        amenity.save()
        amenities.append(amenity)
    
    return amenities


def create_places(locations, users, amenities):
    """Create diverse places with different configurations"""
    print("Creating Places...")
    
    places = []
    hosts = users['hosts']
    cities = locations['cities']
    
    # San Francisco Places
    sf = next(city for city in cities if city.name == "San Francisco")
    
    place1 = Place(
        city_id=sf.id,
        user_id=hosts[0].id,
        name="Cozy Studio in Downtown SF",
        description="A beautiful studio apartment in the heart of San Francisco. Perfect for business travelers and tourists. Walking distance to Union Square and public transportation.",
        number_rooms=1,
        number_bathrooms=1, 
        max_guest=2,
        price_by_night=120,
        latitude=37.7749,
        longitude=-122.4194
    )
    place1.save()
    # Add amenities (one by one, not as a list)
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[5]]:  # WiFi, TV, Kitchen, AC
        place1.amenities = amenity
    places.append(place1)
    
    place2 = Place(
        city_id=sf.id,
        user_id=hosts[1].id,
        name="Luxury Loft with Bay View",
        description="Stunning loft apartment with panoramic views of San Francisco Bay. Modern amenities and prime location in SOMA district.",
        number_rooms=2,
        number_bathrooms=2,
        max_guest=4,
        price_by_night=250,
        latitude=37.7849,
        longitude=-122.4094
    )
    place2.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[5], amenities[7], amenities[16]]:  # WiFi, TV, Kitchen, AC, Pool, City view
        place2.amenities = amenity
    places.append(place2)
    
    # Los Angeles Places
    la = next(city for city in cities if city.name == "Los Angeles")
    
    place3 = Place(
        city_id=la.id,
        user_id=hosts[2].id,
        name="Hollywood Hills Retreat",
        description="Secluded house in the Hollywood Hills with pool and amazing city views. Perfect for groups and special occasions.",
        number_rooms=4,
        number_bathrooms=3,
        max_guest=8,
        price_by_night=400,
        latitude=34.0928,
        longitude=-118.3287
    )
    place3.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[5], amenities[7], amenities[10], amenities[16]]:
        place3.amenities = amenity
    places.append(place3)
    
    place4 = Place(
        city_id=la.id,
        user_id=hosts[0].id,
        name="Venice Beach Apartment",
        description="Steps from Venice Beach! Enjoy the California lifestyle in this beachfront apartment with ocean views.",
        number_rooms=1,
        number_bathrooms=1,
        max_guest=3,
        price_by_night=180,
        latitude=33.9850,
        longitude=-118.4695
    )
    place4.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[14], amenities[16]]:  # WiFi, TV, Kitchen, Beach access, City view
        place4.amenities = amenity
    places.append(place4)
    
    # New York Places
    nyc = next(city for city in cities if city.name == "New York City")
    
    place5 = Place(
        city_id=nyc.id,
        user_id=hosts[1].id,
        name="Manhattan Studio Near Central Park",
        description="Charming studio apartment just blocks from Central Park. Perfect location for exploring NYC with easy subway access.",
        number_rooms=1,
        number_bathrooms=1,
        max_guest=2,
        price_by_night=200,
        latitude=40.7829,
        longitude=-73.9654
    )
    place5.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[6]]:  # WiFi, TV, Kitchen, Heating
        place5.amenities = amenity
    places.append(place5)
    
    place6 = Place(
        city_id=nyc.id,
        user_id=hosts[2].id,
        name="Brooklyn Loft with Rooftop",
        description="Spacious loft in trendy Brooklyn neighborhood. Features rooftop access with Manhattan skyline views.",
        number_rooms=3,
        number_bathrooms=2,
        max_guest=6,
        price_by_night=320,
        latitude=40.6892,
        longitude=-73.9442
    )
    place6.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[6], amenities[12], amenities[16]]:
        place6.amenities = amenity
    places.append(place6)
    
    # Miami Places
    miami = next(city for city in cities if city.name == "Miami")
    
    place7 = Place(
        city_id=miami.id,
        user_id=hosts[0].id,
        name="South Beach Ocean View Condo",
        description="Luxury condo on South Beach with direct ocean access. Modern amenities and vibrant nightlife at your doorstep.",
        number_rooms=2,
        number_bathrooms=2,
        max_guest=4,
        price_by_night=350,
        latitude=25.7907,
        longitude=-80.1300
    )
    place7.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[5], amenities[7], amenities[14]]:
        place7.amenities = amenity
    places.append(place7)
    
    # Austin Places  
    austin = next(city for city in cities if city.name == "Austin")
    
    place8 = Place(
        city_id=austin.id,
        user_id=hosts[1].id,
        name="Music District House",
        description="Hip house in Austin's famous music district. Walking distance to live music venues, restaurants, and downtown.",
        number_rooms=3,
        number_bathrooms=2,
        max_guest=6,
        price_by_night=220,
        latitude=30.2672,
        longitude=-97.7431
    )
    place8.save()
    for amenity in [amenities[0], amenities[1], amenities[2], amenities[5], amenities[13], amenities[17]]:
        place8.amenities = amenity
    places.append(place8)
    
    return places


def create_reviews(places, users):
    """Create realistic reviews for places"""
    print("Creating Reviews...")
    
    guests = users['guests']
    reviews = []
    
    review_data = [
        {
            'place': 0,  # Cozy Studio in Downtown SF
            'user': 0,   # Alice
            'text': "Perfect location for exploring San Francisco! The studio was clean, well-equipped, and John was a great host. Walking distance to everything we wanted to see. Highly recommend!",
            'stars': 5
        },
        {
            'place': 0,
            'user': 1,   # Bob
            'text': "Great value for money in SF. The space is small but has everything you need. Host was responsive and helpful.",
            'stars': 4
        },
        {
            'place': 1,  # Luxury Loft with Bay View
            'user': 2,   # Emma
            'text': "Absolutely stunning views and a beautiful space! Sarah was an excellent host and the amenities were top-notch. Worth every penny.",
            'stars': 5
        },
        {
            'place': 1,
            'user': 0,   # Alice
            'text': "The loft is gorgeous and the location is perfect. Pool access was a nice bonus. Only minor issue was some street noise at night.",
            'stars': 4
        },
        {
            'place': 2,  # Hollywood Hills Retreat
            'user': 1,   # Bob
            'text': "Amazing house for our group vacation! The pool and views were incredible. Mike was very accommodating and the house had everything we needed.",
            'stars': 5
        },
        {
            'place': 3,  # Venice Beach Apartment
            'user': 2,   # Emma
            'text': "Can't beat the location - literally steps from the beach! Apartment was exactly as described. Perfect for a beach getaway.",
            'stars': 5
        },
        {
            'place': 4,  # Manhattan Studio Near Central Park
            'user': 0,   # Alice
            'text': "Fantastic location near Central Park. The studio is cozy and has everything needed for a NYC stay. Sarah was very helpful with recommendations.",
            'stars': 4
        },
        {
            'place': 5,  # Brooklyn Loft with Rooftop
            'user': 1,   # Bob
            'text': "Loved the rooftop access and Brooklyn vibe. Spacious loft perfect for our group. Easy subway access to Manhattan.",
            'stars': 5
        },
        {
            'place': 6,  # South Beach Ocean View Condo
            'user': 2,   # Emma
            'text': "Luxury at its finest! The ocean views were breathtaking and the condo had all high-end amenities. Perfect Miami experience.",
            'stars': 5
        },
        {
            'place': 7,  # Music District House
            'user': 0,   # Alice
            'text': "Great location for experiencing Austin's music scene. The house was comfortable and Sarah provided excellent local recommendations.",
            'stars': 4
        }
    ]
    
    for review_info in review_data:
        review = Review(
            place_id=places[review_info['place']].id,
            user_id=guests[review_info['user']].id,
            text=review_info['text'],
            stars=review_info['stars']
        )
        review.save()
        reviews.append(review)
    
    return reviews


def display_summary():
    """Display a summary of created data"""
    print("\n" + "="*60)
    print("SAMPLE DATA CREATION COMPLETE!")
    print("="*60)
    
    # Count objects
    states = storage.all('State')
    cities = storage.all('City') 
    users = storage.all('User')
    amenities = storage.all('Amenity')
    places = storage.all('Place')
    reviews = storage.all('Review')
    
    print(f"✅ States: {len(states)}")
    print(f"✅ Cities: {len(cities)}")
    print(f"✅ Users: {len(users)}")
    print(f"✅ Amenities: {len(amenities)}")
    print(f"✅ Places: {len(places)}")
    print(f"✅ Reviews: {len(reviews)}")
    
    print("\n" + "="*60)
    print("TESTING ENDPOINTS:")
    print("="*60)
    print("API Server (port 5000):")
    print("  curl http://localhost:5000/api/v1/states")
    print("  curl http://localhost:5000/api/v1/cities")
    print("  curl http://localhost:5000/api/v1/users")
    print("  curl http://localhost:5000/api/v1/amenities")
    print("  curl http://localhost:5000/api/v1/places")
    print("  curl http://localhost:5000/api/v1/places/[place_id]/reviews")
    
    print("\nWeb Interface (port 5001):")
    print("  http://localhost:5001/100-hbnb/")
    
    print("\nConsole Commands:")
    print("  ./console.py")
    print("  (hbnb) all State")
    print("  (hbnb) all Place")
    print("  (hbnb) show Place [place_id]")
    
    print("\n" + "="*60)
    print("SAMPLE PLACES CREATED:")
    print("="*60)
    
    for place in places.values():
        city = next(city for city in storage.all('City').values() if city.id == place.city_id)
        state = next(state for state in storage.all('State').values() if state.id == city.state_id)
        print(f"۩ {place.name} - {city.name}, {state.name}")
        print(f"   ${place.price_by_night}/night | {place.max_guest} guests | {place.number_rooms} rooms")
        print(f"   ID: {place.id}")
        print()


def main():
    """Main function to populate all sample data"""
    print("Starting AirBnB Clone Sample Data Population...")
    print("This will create comprehensive sample data to demonstrate all features.\n")
    
    # Create all sample data
    locations = create_states_and_cities()
    users = create_users()
    amenities = create_amenities()
    places = create_places(locations, users, amenities)
    reviews = create_reviews(places, users)
    
    # Save all data
    storage.save()
    
    # Display summary
    display_summary()


if __name__ == "__main__":
    main()
