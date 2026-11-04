"""Keep only the columns used by milestone1.ipynb: 2019_FPA_FOD_cons.csv -> 2019_FPA_FOD_light.csv (same for 2020)."""
import pandas as pd

COLS = [
    "STATE", "FIRE_SIZE", "DISCOVERY_DATE", "DISCOVERY_DOY", "DISCOVERY_TIME",  # target and time
    "LATITUDE", "LONGITUDE", "pr", "tmmx", "rmin", "vs", "vpd", "erc", "bi", "fm100", "fm1000",
    "Aridity_index", "MOD_NDVI_12m", "Land_Cover_1km", "FRG_1km", "Elevation", "Slope", "TRI",
    "Popo_1km", "GHM", "No_FireStation_10.0km", "SDI", "NPL", "GACC_PL", "RPL_THEMES", "GAP_Sts",
    "road_county_dis", "road_interstate_dis", "road_common_name_dis",
    "road_other_dis", "road_state_dis", "road_US_dis",
]

for year in (2019, 2020):
    df = pd.read_csv(f"{year}_FPA_FOD_cons.csv", usecols=COLS, low_memory=False)
    df[COLS].to_csv(f"{year}_FPA_FOD_light.csv", index=False)
    print(year, df.shape)
