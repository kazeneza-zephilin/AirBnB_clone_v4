$("document").ready(function () {
    const api = "http://" + window.location.hostname;

    // Check API status
    $.get(api + ":5002/api/v1/status/", function (response) {
        if (response.status === "OK") {
            $("DIV#api_status").addClass("available");
        } else {
            $("DIV#api_status").removeClass("available");
        }
    });

    // Load all places initially
    $.ajax({
        url: api + ":5002/api/v1/places_search/",
        type: "POST",
        data: "{}",
        contentType: "application/json",
        dataType: "json",
        success: appendPlaces,
    });

    let states = {};
    $('.locations > UL > H2 > INPUT[type="checkbox"]').change(function () {
        if ($(this).is(":checked")) {
            states[$(this).attr("data-id")] = $(this).attr("data-name");
        } else {
            delete states[$(this).attr("data-id")];
        }
        const locations = Object.assign({}, states, cities);
        if (Object.values(locations).length === 0) {
            $(".locations H4").html("&nbsp;");
        } else {
            $(".locations H4").text(Object.values(locations).join(", "));
        }
    });

    let cities = {};
    $('.locations > UL > UL > LI INPUT[type="checkbox"]').change(function () {
        if ($(this).is(":checked")) {
            cities[$(this).attr("data-id")] = $(this).attr("data-name");
        } else {
            delete cities[$(this).attr("data-id")];
        }
        const locations = Object.assign({}, states, cities);
        if (Object.values(locations).length === 0) {
            $(".locations H4").html("&nbsp;");
        } else {
            $(".locations H4").text(Object.values(locations).join(", "));
        }
    });

    let amenities = {};
    $('.amenities INPUT[type="checkbox"]').change(function () {
        if ($(this).is(":checked")) {
            amenities[$(this).attr("data-id")] = $(this).attr("data-name");
        } else {
            delete amenities[$(this).attr("data-id")];
        }
        if (Object.values(amenities).length === 0) {
            $(".amenities H4").html("&nbsp;");
        } else {
            $(".amenities H4").text(Object.values(amenities).join(", "));
        }
    });

    $("BUTTON").click(function () {
        $.ajax({
            url: api + ":5002/api/v1/places_search/",
            type: "POST",
            data: JSON.stringify({
                states: Object.keys(states),
                cities: Object.keys(cities),
                amenities: Object.keys(amenities),
            }),
            contentType: "application/json",
            dataType: "json",
            success: appendPlaces,
        });
    });
});

function appendPlaces(data) {
    $("SECTION.places").empty();
    $("SECTION.places").append("<H1>Places</H1>");

    data.forEach(function (place) {
        const placeArticle = createPlaceCard(place);
        $("SECTION.places").append(placeArticle);
    });
}

function createPlaceCard(place) {
    const api = "http://" + window.location.hostname;

    return `<ARTICLE class="place-card" data-place-id="${place.id}">
        <DIV class="title">
            <H2>${place.name}</H2>
            <DIV class="price_by_night">
                $${place.price_by_night}
            </DIV>
        </DIV>
        
        <DIV class="information">
            <DIV class="max_guest">
                <I class="fa fa-users fa-3x" aria-hidden="true"></I>
                <BR>
                ${place.max_guest} Guests
            </DIV>
            <DIV class="number_rooms">
                <I class="fa fa-bed fa-3x" aria-hidden="true"></I>
                <BR>
                ${place.number_rooms} Bedrooms
            </DIV>
            <DIV class="number_bathrooms">
                <I class="fa fa-bath fa-3x" aria-hidden="true"></I>
                <BR>
                ${place.number_bathrooms} Bathrooms
            </DIV>
        </DIV>
        
        <DIV class="description">
            ${place.description}
        </DIV>
        
        <DIV class="place-stats">
            <DIV class="stat-item">
                <I class="fa fa-map-marker stat-icon"></I>
                <SPAN id="location-${place.id}">Loading location...</SPAN>
            </DIV>
            <DIV class="stat-item">
                <I class="fa fa-user stat-icon"></I>
                <SPAN id="host-${place.id}">Loading host...</SPAN>
            </DIV>
        </DIV>
        
        <DIV class="amenities-section" id="amenities-${place.id}">
            <DIV class="amenities-title">Amenities</DIV>
            <DIV class="amenities-list">
                Loading amenities...
            </DIV>
        </DIV>
        
        <DIV class="reviews-section">
            <DIV class="reviews-header">
                <H3 class="reviews-title" id="reviews-count-${place.id}">Reviews</H3>
                <BUTTON class="toggle-reviews" data-place-id="${place.id}">
                    Show reviews
                </BUTTON>
            </DIV>
            <DIV class="reviews-container" id="reviews-${place.id}">
                <P class="no-reviews">Loading reviews...</P>
            </DIV>
        </DIV>
    </ARTICLE>`;
}

// Load additional data for each place
function loadPlaceDetails(placeId) {
    const api = "http://" + window.location.hostname;

    // Load reviews
    loadReviews(placeId);

    // Load amenities
    loadAmenities(placeId);

    // Load location and host info
    loadLocationAndHost(placeId);
}

function loadReviews(placeId) {
    const api = "http://" + window.location.hostname;

    $.get(`${api}:5002/api/v1/places/${placeId}/reviews`, function (reviews) {
        const reviewsContainer = $(`#reviews-${placeId}`);
        const reviewsCount = $(`#reviews-count-${placeId}`);

        if (reviews.length === 0) {
            reviewsContainer.html('<P class="no-reviews">No reviews yet</P>');
            reviewsCount.text("Reviews");
        } else {
            reviewsCount.text(`Reviews (${reviews.length})`);

            // Load user details for each review
            const reviewPromises = reviews.map((review) => {
                return $.get(`${api}:5002/api/v1/users/${review.user_id}`).then(
                    (user) => ({ ...review, user })
                );
            });

            Promise.all(reviewPromises).then((reviewsWithUsers) => {
                const reviewsHtml = reviewsWithUsers
                    .map((review) => {
                        const stars = generateStars(review.stars || 5);
                        const reviewDate = new Date(
                            review.created_at
                        ).toLocaleDateString();

                        return `
                        <DIV class="review-item">
                            <DIV class="review-header">
                                <SPAN class="review-author">${
                                    review.user.first_name
                                } ${review.user.last_name}</SPAN>
                                <SPAN class="review-date">${reviewDate}</SPAN>
                            </DIV>
                            ${
                                review.stars
                                    ? `
                            <DIV class="review-rating">
                                <SPAN class="stars">${stars}</SPAN>
                                <SPAN class="rating-number">${review.stars}/5</SPAN>
                            </DIV>`
                                    : ""
                            }
                            <P class="review-text">${review.text}</P>
                        </DIV>
                    `;
                    })
                    .join("");

                reviewsContainer.html(reviewsHtml);
            });
        }
    }).fail(function () {
        $(`#reviews-${placeId}`).html(
            '<P class="no-reviews">Failed to load reviews</P>'
        );
    });
}

function loadAmenities(placeId) {
    const api = "http://" + window.location.hostname;

    // Get place details to find amenity_ids
    $.get(
        `${api}:5002/api/v1/places_search`,
        {},
        function (places) {
            const place = places.find((p) => p.id === placeId);
            if (place && place.amenity_ids && place.amenity_ids.length > 0) {
                // Load amenity details
                const amenityPromises = place.amenity_ids.map((amenityId) => {
                    return $.get(`${api}:5002/api/v1/amenities/${amenityId}`);
                });

                Promise.all(amenityPromises)
                    .then((amenities) => {
                        const amenitiesHtml = amenities
                            .map(
                                (amenity) =>
                                    `<SPAN class="amenity-tag">${amenity.name}</SPAN>`
                            )
                            .join("");

                        $(`#amenities-${placeId} .amenities-list`).html(
                            amenitiesHtml
                        );
                    })
                    .catch(() => {
                        $(`#amenities-${placeId} .amenities-list`).html(
                            '<SPAN class="amenity-tag">WiFi</SPAN>'
                        );
                    });
            } else {
                $(`#amenities-${placeId} .amenities-list`).html(
                    '<SPAN style="color: #767676; font-style: italic;">No amenities listed</SPAN>'
                );
            }
        },
        "json"
    ).fail(function () {
        $(`#amenities-${placeId} .amenities-list`).html(
            '<SPAN style="color: #767676;">Failed to load amenities</SPAN>'
        );
    });
}

function loadLocationAndHost(placeId) {
    const api = "http://" + window.location.hostname;

    // Get place details first
    $.post(
        `${api}:5002/api/v1/places_search`,
        "{}",
        function (places) {
            const place = places.find((p) => p.id === placeId);
            if (place) {
                // Load city and state info
                $.get(
                    `${api}:5002/api/v1/cities/${place.city_id}`,
                    function (city) {
                        $.get(
                            `${api}:5002/api/v1/states/${city.state_id}`,
                            function (state) {
                                $(`#location-${placeId}`).text(
                                    `${city.name}, ${state.name}`
                                );
                            }
                        ).fail(function () {
                            $(`#location-${placeId}`).text(city.name);
                        });
                    }
                ).fail(function () {
                    $(`#location-${placeId}`).text("Location unavailable");
                });

                // Load host info
                $.get(
                    `${api}:5002/api/v1/users/${place.user_id}`,
                    function (user) {
                        $(`#host-${placeId}`).html(
                            `Hosted by <SPAN class="host-name">${user.first_name} ${user.last_name}</SPAN>`
                        );
                    }
                ).fail(function () {
                    $(`#host-${placeId}`).text("Host information unavailable");
                });
            }
        },
        "json"
    );
}

function generateStars(rating) {
    const fullStars = Math.floor(rating);
    const hasHalfStar = rating % 1 !== 0;
    let stars = "";

    for (let i = 0; i < fullStars; i++) {
        stars += "★";
    }

    if (hasHalfStar) {
        stars += "☆";
    }

    return stars;
}

// Event handlers
$(document).on("click", ".toggle-reviews", function () {
    const placeId = $(this).data("place-id");
    const reviewsContainer = $(`#reviews-${placeId}`);
    const button = $(this);

    if (reviewsContainer.hasClass("active")) {
        reviewsContainer.removeClass("active");
        button.text("Show reviews");
    } else {
        reviewsContainer.addClass("active");
        button.text("Hide reviews");

        // Load reviews if not already loaded
        if (
            reviewsContainer.find(".no-reviews").text() === "Loading reviews..."
        ) {
            loadReviews(placeId);
        }
    }
});

// Load additional details when places are added
$(document).on("DOMNodeInserted", "ARTICLE.place-card", function () {
    const placeId = $(this).data("place-id");
    if (placeId) {
        loadPlaceDetails(placeId);
    }
});
