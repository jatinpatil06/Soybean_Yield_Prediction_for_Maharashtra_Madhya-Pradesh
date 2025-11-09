import pandas as pd

weather_data = pd.read_csv("weather_data.csv")
yield_data = pd.read_csv("mp_mh_yield_data.csv")
soil_data = pd.read_csv("soil_data_reduced.csv")

yield_data.rename(columns = {'Dist Name' : 'DISTRICT', 'Year' : 'YEAR', 'SOYABEAN AREA (1000 ha)' : 'AREA', 'SOYABEAN YIELD (Kg per ha)' : 'YIELD'}, inplace = True)
yield_data = yield_data[['YEAR', 'DISTRICT', 'AREA', 'YIELD']]
merged_data_1 = pd.merge(yield_data, weather_data, on = ['DISTRICT', 'YEAR'], how = 'inner')
print(merged_data_1.head())
merged_data_2 = pd.merge(merged_data_1, soil_data, on = ['DISTRICT'], how = 'inner')
print(merged_data_2.head())

merged_data_2.to_csv("merged_data.csv", index = False)