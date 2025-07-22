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

// Simple place cards for the main page
function appendPlaces(data) {
    $("SECTION.places").empty();
    $("SECTION.places").append("<H1>Places</H1>");

    data.forEach(function (place) {
        const placeCard = createSimplePlaceCard(place);
        $("SECTION.places").append(placeCard);
    });
}

function createSimplePlaceCard(place) {
    return `
        <ARTICLE class="place-card simple-card" data-place-id="${place.id}">
            <DIV class="place-image">
                <IMG src="/static/images/icon_house.png" alt="${
                    place.name
                }" class="place-photo">
                <DIV class="price-overlay">$${place.price_by_night}/night</DIV>
            </DIV>
            
            <DIV class="place-info">
                <H3 class="place-title">${place.name}</H3>
                
                <DIV class="place-basics">
                    <SPAN class="basic-info">
                        <I class="fa fa-users"></I> ${place.max_guest} guests
                    </SPAN>
                    <SPAN class="basic-info">
                        <I class="fa fa-bed"></I> ${place.number_rooms} bedrooms
                    </SPAN>
                    <SPAN class="basic-info">
                        <I class="fa fa-bath"></I> ${
                            place.number_bathrooms
                        } bathrooms
                    </SPAN>
                </DIV>
                
                <P class="place-description">${truncateText(
                    place.description,
                    100
                )}</P>
            </DIV>
        </ARTICLE>
    `;
}

// Helper functions
function truncateText(text, maxLength) {
    if (text.length <= maxLength) return text;
    return text.substring(0, maxLength) + "...";
}

// Event handlers
$(document).on("click", ".place-card", function () {
    const placeId = $(this).data("place-id");
    window.location.href = `/100-hbnb/place/${placeId}`;
});
