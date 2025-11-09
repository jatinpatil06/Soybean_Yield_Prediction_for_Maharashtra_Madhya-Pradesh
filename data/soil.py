import requests

# Define coordinates for the location of interest
latitude = 19.0760  # Example for Mumbai
longitude = 72.8777

# SoilGrids API endpoint
url = f"https://rest.soilgrids.org/query?lon={longitude}&lat={latitude}&depth=0-5cm"

# Make a GET request
response = requests.get(url)

# Parse the JSON response
if response.status_code == 200:
    soil_data = response.json()
    print(soil_data)
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
