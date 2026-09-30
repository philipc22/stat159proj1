# Replicating Global Temperature Anomaly Graphics

Philip Chiu, Stat 159, Project 1

## Overview
This project replicates four graphics of global temperature anomalies using
NASA GISS Surface Temperature Analysis (GISTEMP v4) data. Graphics 1-3 come
from NASA's GISTEMP website. Graphic 4 replicates the New York Times line chart
"Rising Global Temperature" (Schwartz and Popovich, Feb 6, 2019), which is a
modified version of Graphic 3.

## Data Source
NASA GISS GISTEMP v4: https://data.giss.nasa.gov/gistemp/data_v4.html

| File in `data/` | Used for |
|---|---|
| `graphic1_land_ocean.csv` | Graphic 1: anomalies over land and ocean |
| `graphic2_seasonal_cycle.csv` | Graphic 2: seasonal cycle since 1880 |
| `graphic3_global_mean.csv` | Graphics 3 and 4: global annual mean |

**Note on data collection:** `scripts/download_data.py` downloads these files.
When I ran it on the course JupyterHub, NASA's server refused the connection, so
the three CSVs in `data/` were downloaded manually in a browser from the same URLs.
The script is included for reproducibility.

## Repository Structure
```
README.md
requirements.txt
ai_documentation.txt
data/raw GISTEMP CSV files
scripts/download script and one notebook per graphic
outputs/figures saved as PNG and PDF
report/executive summary with the four figures
```

## Setup
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## How to Reproduce
1. (Optional) `python scripts/download_data.py` to re-download the data.
2. Run the notebooks in `scripts/`, one per graphic.
3. Figures are saved to `outputs/` as PNG and PDF.
4. The report is in `report/`.

## Graphics
To be completed.

## Git Workflow
Work was done on separate branches (`data-download`, `graphic-1`, `graphic-2`,
`graphic-3`, `graphic-4`, `report`) and merged into `main` through pull requests.

## Notes on Differences from Originals
To be completed.

## AI Assistance
Prompts and outputs are logged in `ai_documentation.txt`.

## Credits
Data and original graphics: NASA GISS / GISTEMP v4. Graphic 4 is based on the
New York Times article "It's Official: 2018 Was the Fourth-Warmest Year on Record."