"""Download the raw GISTEMP v4 data files into the data/ folder.

Run from anywhere with: python scripts/download_data.py

Python version 3.14.7

Source: NASA GISS Surface Temperature Analysis 
https://data.giss.nasa.gov/gistemp/data_v4.html

Note on how the files in data/ were actually obtained:
When I ran this script on Berkeley DataHub, the first file
downloaded, but after that data.giss.nasa.gov started refusing every
connection from DataHub ("Connection refused"), while other sites like
github.com still worked. The same URLs opened fine in my own browser, so
it looks like NASA's server was blocking DataHub, not a bug in this code.
To keep working, I downloaded the three CSVs from the URLs in FILES below
in my browser, saved them with the filenames this script uses, and uploaded
them to data/ without editing them.
"""
from pathlib import Path

import requests

# Build paths
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

BASE_URL = "https://data.giss.nasa.gov/gistemp/graphs_v4/graph_data"

# Local filename -> source URL
FILES = {
    "graphic1_land_ocean.csv":
        f"{BASE_URL}/Temperature_Anomalies_over_Land_and_over_Ocean/graph.csv",
    "graphic2_seasonal_cycle.csv":
        f"{BASE_URL}/GISTEMP_Seasonal_Cycle_since_1880/graph.csv",
    "graphic3_global_mean.csv":
        f"{BASE_URL}/Global_Mean_Estimates_based_on_Land_and_Ocean_Data/graph.csv",
}

HEADERS = {"User-Agent": "Mozilla/5.0"}


def download(filename: str, url: str) -> None:
    """Download one file and save it in DATA_DIR."""
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status() 

    
    if response.text.lstrip().lower().startswith("<"):
        raise ValueError(f"{filename}: got HTML instead of CSV from {url}")

    (DATA_DIR / filename).write_bytes(response.content)
    print(f"Saved {filename} ({len(response.content):,} bytes)")



if __name__ == "__main__":
    for name, link in FILES.items():
        download(name, link)
    print(f"Done. Files are in {DATA_DIR}")