// Fetching limo tracking data from the server
async function getTrackingData() {
    const response = await fetch('/api/tracking/');
    const trackingData = await response.json();
    return trackingData;
}

// Updating the tracking map with the latest data
function updateTrackingMap(trackingData) {
    const trackingMap = document.getElementById('tracking-map');

    // Clear the map
    trackingMap.innerHTML = '';

    // Add new tracking data to the map
    trackingData.forEach((tracking) => {
        const marker = document.createElement('div');
        marker.classList.add('marker');
        marker.style.left = `${tracking.current_location.longitude}%`;
        marker.style.top = `${tracking.current_location.latitude}%`;
        trackingMap.appendChild(marker);
    });
}

// Fetching and updating the tracking data every 5 seconds
setInterval(async () => {
    const trackingData = await getTrackingData();
    updateTrackingMap(trackingData);
}, 5000);