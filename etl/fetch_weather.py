import requests
import fastf1

fastf1.Cache.enable_cache('./etl/cache/') # Avoid downloading the same data multiple times

CIRCUIT_COORDINATES = {
    "Sakhir": {"lat": 26.0325, "lon": 50.5106},
    "Jeddah": {"lat": 21.6319, "lon": 39.1044},
    "Melbourne": {"lat": -37.8497, "lon": 144.968},
    "Baku": {"lat": 40.3725, "lon": 49.8533},
    "Miami": {"lat": 25.9581, "lon": -80.2389},
    "Barcelona": {"lat": 41.57, "lon": 2.261},
    "Monaco": {"lat": 43.7347, "lon": 7.4206},
    "Montreal": {"lat": 45.5048, "lon": -73.5268},
    "Silverstone": {"lat": 52.0786, "lon": -1.0169},
    "Spielberg": {"lat": 46.8497, "lon": 14.7644},
    "Budapest": {"lat": 47.5789, "lon": 19.2486},
    "Spa-Francorchamps": {"lat": 50.4372, "lon": 5.9714},
    "Zandvoort": {"lat": 52.3888, "lon": 4.5408},
    "Monza": {"lat": 45.6156, "lon": 9.2811},
    "Marina Bay": {"lat": 1.2914, "lon": 103.8644},
    "Suzuka": {"lat": 34.8431, "lon": 136.5414},
    "Lusail": {"lat": 25.4900, "lon": 51.4542},
    "Austin": {"lat": 30.1328, "lon": -97.6411},
    "Mexico City": {"lat": 19.4042, "lon": -99.0908},
    "São Paulo": {"lat": -23.7036, "lon": -46.6997},
    "Las Vegas": {"lat": 36.1699, "lon": -115.1398},
    "Yas Island": {"lat": 24.4672, "lon": 54.6031},
}

def fetch_weather_data(circuit: str, date: str, race_hour: int) -> dict:
    """Fetches weather data for a given circuit, date and race hour."""
    if circuit not in CIRCUIT_COORDINATES:
        raise ValueError(f"Circuit '{circuit}' not found in coordinates mapping.")
    
    coords = CIRCUIT_COORDINATES[circuit]
    response = requests.get(
        "https://archive-api.open-meteo.com/v1/archive",
        params={
            "latitude": coords['lat'],
            "longitude": coords['lon'],
            "start_date": date,
            "end_date": date,
            "hourly": "temperature_2m,precipitation,windspeed_10m"
        }
    )
    
    data = response.json()['hourly']
    window = slice(race_hour, race_hour + 2)
    precip_sum = sum(data['precipitation'][window])

    return {
        "temp_avg": sum(data['temperature_2m'][window]) / 2,
        "precipitation_sum": precip_sum,
        "windspeed_avg": sum(data['windspeed_10m'][window]) / 2,
        "is_wet": precip_sum > 1.0
    }
