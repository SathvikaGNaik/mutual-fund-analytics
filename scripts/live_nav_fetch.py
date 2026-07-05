import requests
import pandas as pd
from pathlib import Path

# Create output folder if it doesn't exist
output_folder = Path("data/raw/live_nav")
output_folder.mkdir(parents=True, exist_ok=True)

# Scheme codes from the project
schemes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_Large_Cap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for scheme_name, scheme_code in schemes.items():

    print(f"\nFetching {scheme_name}...")

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav = pd.DataFrame(data["data"])

        file_path = output_folder / f"{scheme_name}.csv"

        nav.to_csv(file_path, index=False)

        print(f"Saved -> {file_path}")

    else:
        print(f"Failed for {scheme_name}")