import requests
import gps

def get_location_by_ip():
    try:
        response = requests.get('https://ipinfo.io/json')
        data = response.json()
        location = {
            'ip': data.get('ip'),
            'city': data.get('city'),
            'region': data.get('region'),
            'country': data.get('country'),
            'loc': data.get('loc')  # Latitude and Longitude
        }
        return location
    except requests.RequestException as e:
        print(f"Error fetching location data: {e}")
        return None

def get_gps_coordinates():
    try:
        session = gps.gps("localhost", "2947")
        session.stream(gps.WATCH_ENABLE | gps.WATCH_NEWSTYLE)
        report = session.next()
        if report['class'] == 'TPV':
            latitude = getattr(report, 'lat', 'Unavailable')
            longitude = getattr(report, 'lon', 'Unavailable')
            return latitude, longitude
    except Exception as e:
        print(f"Error fetching GPS data: {e}")
        return None

def main():
    # Choose method:
    # Uncomment the desired method to use
    
    # IP Geolocation
    print("Fetching location using IP geolocation...")
    location = get_location_by_ip()
    if location:
        print(f"IP Address: {location['ip']}")
        print(f"City: {location['city']}")
        print(f"Region: {location['region']}")
        print(f"Country: {location['country']}")
        print(f"Coordinates: {location['loc']}")

    # GPS Module
    # Uncomment the following section if using GPS hardware
    """
    print("Fetching GPS coordinates...")
    coordinates = get_gps_coordinates()
    if coordinates:
        print(f"Latitude: {coordinates[0]}")
        print(f"Longitude: {coordinates[1]}")
    """

if __name__ == "__main__":
    main()
