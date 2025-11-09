import pandas as pd
mh_coord = pd.read_csv("mh_coord.csv")
mp_coord = pd.read_csv("mp_coord.csv")
print(mh_coord.shape, mp_coord.shape)
combined_coord = pd.concat([mp_coord, mh_coord], ignore_index=True)
combined_coord.to_csv("district_coordinates.csv", index = False)