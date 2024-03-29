document.addEventListener("DOMContentLoaded", function() {
    var venueSelect = document.getElementById("venue-select");
    var performerSelect = document.getElementById("performer-select");
    var genreSelect = document.getElementById("genre-select");
    var gigList = document.getElementById("gig-list");
    var gigs = gigList.getElementsByTagName("li");
    var sortSelect = document.getElementById("sort-select");

    venueSelect.addEventListener("change", filterGigs);
    performerSelect.addEventListener("change", filterGigs);
    genreSelect.addEventListener("change", filterGigs);
    sortSelect.addEventListener("change", sortGigs);
    
    function filterGigs() {
        var selectedVenueId = venueSelect.value;
        var selectedPerformerId = performerSelect.value;
        var selectedGenre = genreSelect.value;
        
        for (var i = 0; i < gigs.length; i++) {
            var gigVenueId = gigs[i].getAttribute("data-venue");
            var gigPerformersIds = gigs[i].getAttribute("data-performers");
            var gigGenres = gigs[i].getAttribute("data-genres");

            var venueMatch = selectedVenueId === "" || gigVenueId === selectedVenueId;
            var performerMatch = selectedPerformerId === "" || gigPerformersIds.includes(selectedPerformerId);
            var genreMatch = selectedGenre === "" || gigGenres.includes(selectedGenre);
            
            if (venueMatch && performerMatch && genreMatch) {
                gigs[i].style.display = "block";
            } else {
                gigs[i].style.display = "none";
            }
        }
    };

    function sortGigs() {
        var sortOrder = sortSelect.value;
        var sortedGigs;
        
        if (sortOrder === 'default') {
            sortedGigs = Array.from(gigs).sort(function(a, b) {
                var idA = parseInt(a.getAttribute("data-id"));
                var idB = parseInt(b.getAttribute("data-id"));
                return idA - idB;
            });
        } else if (sortOrder === 'asc' || sortOrder === 'desc') {
            sortedGigs = Array.from(gigs).sort(function(a, b) {
                var nameA = a.querySelector("a").innerText.toLowerCase();
                var nameB = b.querySelector("a").innerText.toLowerCase();
                if (sortOrder === 'asc') {
                    return nameA.localeCompare(nameB);
                } else {
                    return nameB.localeCompare(nameA);
                }
            });
        } else if (sortOrder === 'soon' || sortOrder === 'leastSoon') {
            sortedGigs = Array.from(gigs).sort(function(a, b) {
                var dateA = parseInt(a.getAttribute("data-date"));
                var dateB = parseInt(b.getAttribute("data-date"));
                var timeA = parseInt(a.getAttribute("data-time"));
                var timeB = parseInt(b.getAttribute("data-time"));
                if (sortOrder === 'soon') {
                    if (dateA === dateB){
                        return timeA - timeB;
                    }
                    return dateA - dateB;
                } else {
                    if (dateA === dateB){
                        return timeB - timeA;
                    }
                    return dateB - dateA;
                }
            });
        }

        while (gigList.firstChild) {
            gigList.removeChild(gigList.firstChild);
        }

        sortedGigs.forEach(function(gig) {
            gigList.appendChild(gig);
        });
    };
});