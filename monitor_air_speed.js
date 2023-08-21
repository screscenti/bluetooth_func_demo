async function fetchAirspeed() {
    try {
        const response = await fetch('http://your-esp-ip/airspeed');
        if (response.ok) {
            const data = await response.json();
            console.log('Airspeed:', data.airspeed, 'm/s');
        } else {
            console.error('Failed to fetch airspeed');
        }
    } catch (error) {
        console.error('Error fetching airspeed:', error);
    }
}

// Fetch airspeed every 5 seconds
setInterval(fetchAirspeed, 5000);
