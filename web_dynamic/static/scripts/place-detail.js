$(document).ready(function() {
    const api = "http://" + window.location.hostname;
    const placeId = $("#place-detail-container").attr("data-place-id");
    
    console.log("Page ready, place ID:", placeId);
    
    // Check API status
    $.get(api + ":5002/api/v1/status/", function (response) {
        if (response.status === "OK") {
            $("DIV#api_status").addClass("available");
        } else {
            $("DIV#api_status").removeClass("available");
        }
    });
    
    // Load place details
    if (placeId) {
        loadPlaceDetails(placeId);
    } else {
        console.error("No place ID found");
        showError("Invalid place ID");
    }
});

function loadPlaceDetails(placeId) {
    const api = "http://" + window.location.hostname;
    
    // Load place data
    $.ajax({
        url: `${api}:5002/api/v1/places_search`,
        type: "POST",
        data: "{}",
        contentType: "application/json",
        dataType: "json",
        success: function(places) {
            console.log("Places loaded:", places.length);
            const place = places.find(p => p.id === placeId);
            if (place) {
                console.log("Place found:", place.name);
                loadCompleteDetails(place);
            } else {
                console.log("Place not found with ID:", placeId);
                showError("Property not found");
            }
        },
        error: function(xhr, status, error) {
            console.log("API Error:", status, error);
            showError("Failed to load property details");
        }
    });
}

function loadCompleteDetails(place) {
    const api = "http://" + window.location.hostname;
    
    // Load all data in parallel
    const promises = [
        loadLocationInfo(place.city_id),
        loadHostInfo(place.user_id),
        loadReviews(place.id),
        loadAmenities(place.amenity_ids || [])
    ];
    
    Promise.all(promises).then(([location, host, reviews, amenities]) => {
        console.log("All data loaded successfully");
        const detailsHtml = createPlaceDetailContent(place, location, host, reviews, amenities);
        $("#place-detail-container").html(detailsHtml);
    }).catch((error) => {
        console.log("Error loading complete details:", error);
        showError("Failed to load complete property details");
    });
}

function createPlaceDetailContent(place, location, host, reviews, amenities) {
    const avgRating = reviews.length > 0 ? 
        (reviews.reduce((sum, r) => sum + (r.stars || 5), 0) / reviews.length).toFixed(1) : null;
    
    return `
        <DIV class="place-detail">
            <DIV class="place-hero">
                <IMG src="/static/images/icon_house.png" alt="${place.name}" class="place-hero-image">
                <DIV class="place-hero-overlay">
                    <H1 class="place-title">${place.name}</H1>
                    <DIV class="place-location">
                        <I class="fa fa-map-marker"></I>
                        ${location.city}, ${location.state}
                    </DIV>
                </DIV>
            </DIV>
            
            <DIV class="place-content">
                <DIV class="place-header">
                    <DIV class="place-info">
                        <DIV class="place-basics">
                            <DIV class="basic-stat">
                                <I class="fa fa-users"></I>
                                <SPAN>${place.max_guest} guests</SPAN>
                            </DIV>
                            <DIV class="basic-stat">
                                <I class="fa fa-bed"></I>
                                <SPAN>${place.number_rooms} bedrooms</SPAN>
                            </DIV>
                            <DIV class="basic-stat">
                                <I class="fa fa-bath"></I>
                                <SPAN>${place.number_bathrooms} bathrooms</SPAN>
                            </DIV>
                        </DIV>
                        ${avgRating ? `
                            <DIV class="rating-section">
                                <SPAN class="stars">${generateStars(avgRating)}</SPAN>
                                <SPAN class="rating-text">${avgRating} (${reviews.length} reviews)</SPAN>
                            </DIV>
                        ` : ''}
                    </DIV>
                    
                    <DIV class="price-section">
                        <H2 class="price-main">$${place.price_by_night}</H2>
                        <P class="price-label">per night</P>
                    </DIV>
                </DIV>
                
                <DIV class="place-grid">
                    <DIV class="main-content">
                        <DIV class="description-section">
                            <H3>About this place</H3>
                            <P class="description-text">${place.description}</P>
                        </DIV>
                        
                        ${amenities.length > 0 ? `
                            <DIV class="amenities-section">
                                <H3>Amenities</H3>
                                <DIV class="amenities-grid">
                                    ${amenities.map(amenity => `
                                        <DIV class="amenity-item">
                                            <I class="fa fa-check"></I>
                                            <SPAN>${amenity.name}</SPAN>
                                        </DIV>
                                    `).join('')}
                                </DIV>
                            </DIV>
                        ` : ''}
                        
                        <DIV class="reviews-section">
                            <H3>Reviews</H3>
                            ${createReviewsContent(reviews, avgRating)}
                        </DIV>
                    </DIV>
                    
                    <DIV class="sidebar">
                        <DIV class="host-section">
                            <H3>Hosted by ${host.first_name}</H3>
                            <DIV class="host-card">
                                <DIV class="host-avatar">
                                    <I class="fa fa-user-circle fa-4x"></I>
                                </DIV>
                                <H4 class="host-name">${host.first_name} ${host.last_name}</H4>
                                <P class="host-email">${host.email}</P>
                                <P class="host-joined">Member since ${new Date(host.created_at).getFullYear()}</P>
                            </DIV>
                        </DIV>
                    </DIV>
                </DIV>
            </DIV>
        </DIV>
    `;
}

function createReviewsContent(reviews, avgRating) {
    if (reviews.length === 0) {
        return '<DIV class="no-reviews">No reviews yet. Be the first to review this place!</DIV>';
    }
    
    return `
        ${avgRating ? `
            <DIV class="reviews-summary">
                <DIV class="reviews-rating">
                    <H4 class="rating-big">${avgRating}</H4>
                    <DIV class="rating-stars">${generateStars(avgRating)}</DIV>
                    <P class="rating-count">${reviews.length} reviews</P>
                </DIV>
            </DIV>
        ` : ''}
        
        <DIV class="reviews-list">
            ${reviews.map(review => `
                <DIV class="review-item">
                    <DIV class="review-header">
                        <SPAN class="reviewer-name">${review.user.first_name} ${review.user.last_name}</SPAN>
                        <SPAN class="review-date">${new Date(review.created_at).toLocaleDateString()}</SPAN>
                    </DIV>
                    ${review.stars ? `
                        <DIV class="review-rating">
                            <SPAN class="stars">${generateStars(review.stars)}</SPAN>
                        </DIV>
                    ` : ''}
                    <P class="review-text">${review.text}</P>
                </DIV>
            `).join('')}
        </DIV>
    `;
}

function generateStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 >= 0.5;
    let stars = '';
    
    for (let i = 0; i < fullStars; i++) {
        stars += '★';
    }
    if (hasHalfStar) {
        stars += '☆';
    }
    
    return stars;
}

function loadLocationInfo(cityId) {
    const api = "http://" + window.location.hostname;
    return $.get(`${api}:5002/api/v1/cities/${cityId}`)
        .then(function(city) {
            return $.get(`${api}:5002/api/v1/states/${city.state_id}`)
                .then(function(state) {
                    return { city: city.name, state: state.name };
                });
        })
        .catch(function() {
            return { city: 'Unknown', state: 'Location' };
        });
}

function loadHostInfo(userId) {
    const api = "http://" + window.location.hostname;
    return $.get(`${api}:5002/api/v1/users/${userId}`)
        .catch(function() {
            return { 
                first_name: 'Unknown', 
                last_name: 'Host', 
                email: '', 
                created_at: new Date().toISOString()
            };
        });
}

function loadReviews(placeId) {
    const api = "http://" + window.location.hostname;
    return $.get(`${api}:5002/api/v1/places/${placeId}/reviews`)
        .then(function(reviews) {
            // Load user info for each review
            const userPromises = reviews.map(function(review) {
                return $.get(`${api}:5002/api/v1/users/${review.user_id}`)
                    .then(function(user) {
                        return Object.assign({}, review, { user: user });
                    })
                    .catch(function() {
                        return Object.assign({}, review, { 
                            user: { first_name: 'Anonymous', last_name: 'User' } 
                        });
                    });
            });
            
            return Promise.all(userPromises);
        })
        .catch(function() {
            return [];
        });
}

function loadAmenities(amenityIds) {
    const api = "http://" + window.location.hostname;
    if (!amenityIds || amenityIds.length === 0) {
        return Promise.resolve([]);
    }
    
    const amenityPromises = amenityIds.map(function(id) {
        return $.get(`${api}:5002/api/v1/amenities/${id}`)
            .catch(function() {
                return null;
            });
    });
    
    return Promise.all(amenityPromises)
        .then(function(amenities) {
            return amenities.filter(function(a) { return a !== null; });
        })
        .catch(function() {
            return [];
        });
}

function showError(message) {
    $("#place-detail-container").html(`
        <DIV class="error-message">
            <I class="fa fa-exclamation-triangle"></I>
            <H3 class="error-title">Oops!</H3>
            <P class="error-text">${message}</P>
        </DIV>
    `);
}
