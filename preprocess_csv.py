"""Builds {year}_FPA_FOD_light.csv (only the columns used by milestone1.ipynb) from the Zenodo file {year}_FPA_FOD_cons.csv.
The big file is downloaded if missing; nothing is done if the light file already exists."""
import os
import urllib.request
import pandas as pd

ZENODO = "https://zenodo.org/records/8381129/files/{}?download=1"

COLS = [
    "STATE", "FIRE_SIZE", "DISCOVERY_DATE", "DISCOVERY_DOY", "DISCOVERY_TIME",  # target and time
    "LATITUDE", "LONGITUDE", "pr", "tmmx", "rmin", "vs", "vpd", "erc", "bi", "fm100", "fm1000",
    "Aridity_index", "MOD_NDVI_12m", "Land_Cover_1km", "FRG_1km", "Elevation", "Slope", "TRI",
    "Popo_1km", "GHM", "No_FireStation_10.0km", "SDI", "NPL", "GACC_PL", "RPL_THEMES", "GAP_Sts",
    "road_county_dis", "road_interstate_dis", "road_common_name_dis",
    "road_other_dis", "road_state_dis", "road_US_dis",
]


def prepare(years=(2019, 2020)):
    for year in years:
        raw, light = f"{year}_FPA_FOD_cons.csv", f"{year}_FPA_FOD_light.csv"
        if os.path.exists(light):
            continue
        if not os.path.exists(raw):
            print(f"Downloading {raw} from Zenodo...")
            urllib.request.urlretrieve(ZENODO.format(raw), raw)
        pd.read_csv(raw, usecols=COLS, low_memory=False)[COLS].to_csv(light, index=False)


if __name__ == "__main__":
    prepare()
