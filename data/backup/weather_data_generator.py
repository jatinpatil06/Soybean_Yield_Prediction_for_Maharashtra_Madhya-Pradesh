import requests
import pandas as pd

#range for the weather data
start_year = 1990
end_year = 2018

#defining the parameters for the weather data
param_list = "PS,TS,QV2M,WS2M,T2M_MAX,T2M_MIN,ALLSKY_KT,CLOUD_AMT,PRECTOTCORR,ALLSKY_SFC_UVA,ALLSKY_SFC_UVB,ALLSKY_SFC_SW_DWN,ALLSKY_SFC_PAR_TOT"

#loading the coordinates data
districts = pd.read_csv("district_coordinates.csv")
no_of_rows = districts.shape[0]

#definig the weather dataframe
weather_data = pd.DataFrame(columns = param_list.split(','))

for i in range(5):
    print(f"Requesting data for {districts.iloc[i,0]}")
    district_name = districts.iloc[i,0]
    district_latitude = districts.iloc[i,1]
    district_longitude = districts.iloc[i,2]

    #api to access NASA Power data
    url = f"https://power.larc.nasa.gov/api/temporal/monthly/point?parameters={param_list}&community=AG&longitude={district_longitude}&latitude={district_latitude}&start={start_year}&end={end_year}&format=CSV"

    #getting the raw csv response from the api
    response = requests.get(url)
    if response.status_code == 200:
        print("Request successful.")
        with open("temp.csv", "wb") as file:
            file.write(response.content)
        print("temp file written successfully")
        #converting it into a dataframe while skipping the header data
        district_data = pd.read_csv("temp.csv", skiprows= 21)
        district_data = district_data[['PARAMETER', 'YEAR', 'ANN']]
        #print(data)

        result = district_data.pivot(index = 'YEAR', columns = 'PARAMETER', values = 'ANN')
        result.reset_index(inplace = True)
        result['DISTRICT'] = district_name
        
        weather_data = pd.concat([weather_data, result], ignore_index = True)
        weather_data.to_csv("weather_data.csv", index = False)
        print("+------------------------------------------+\n")

    else:
        print(f"Request failed for {district_name}. Status code : {response.status_code}")

print("Weather data fetching completed.")