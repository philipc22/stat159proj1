Replicating Global Temperature Anomaly Graphics

This project replicates four graphics of global temperature anomalies using NASA GISS Surface Temperature Analysis (GISTEMP v4) data. Graphics 1-3 come from NASA's GISTEMP website. Graphic 4 replicates the New York Times line chart "Rising Global Temperature" (Schwartz and Popovich, Feb 6, 2019), which is a modified version of Graphic 3.

Data Source

NASA GISS GISTEMP v4: https://data.giss.nasa.gov/gistemp/data_v4.html

File in data/	Used for
graphic1_land_ocean.csv	Graphic 1: anomalies over land and ocean
graphic2_seasonal_cycle.csv	Graphic 2: seasonal cycle since 1880
graphic3_global_mean.csv Graphics 3 and 4: global annual mean

Note on data collection: scripts/download_data.py downloads these files. When I ran it on the course JupyterHub, NASA's server refused the connection, so the three CSVs in data/ were downloaded manually in a browser from the same URLs. The script is included for reproducibility.

Repository Structure
README.md              project overview (this file)
requirements.txt       Python packages needed to run the notebooks
ai_documentation.txt   prompts and outputs from AI assistance
.gitignore             files git should ignore
data/                  raw GISTEMP CSV files
scripts/               download script and one notebook per graphic
outputs/               figures saved as PNG and PDF
report/                executive summary with the four figures


Setup

bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

How to Reproduce

(Optional) python scripts/download_data.py to re-download the data.
Run the notebooks in scripts/, one per graphic.
Figures are saved to outputs/ as PNG and PDF.
The report is in report/.

Graphics
Graphic	Notebook	Output
1. Temperature Anomalies over Land and over Ocean	scripts/graphic1_land_ocean.ipynb	outputs/graphic1_land_ocean.png, .pdf
2. GISTEMP Seasonal Cycle since 1880	scripts/graphic2_seasonal_cycle.ipynb	outputs/graphic2_seasonal_cycle.png, .pdf
3. Global Mean Estimates based on Land and Ocean Data	scripts/graphic3_global_mean.ipynb	outputs/graphic3_global_mean.png, .pdf
4. Rising Global Temperature (New York Times)	scripts/graphic4_nyt_replication.ipynb	outputs/graphic4_nyt_replication.png, .pdf

The report with all four figures and a short description of each is report/report.md.

Git Workflow

Work was done on separate branches (data-download, graphic-1, graphic-2, graphic-3, graphic-4, report) and merged into main through pull requests.

Notes on Differences from Originals
All graphics: colors and fonts are approximated by eye with matplotlib.
Graphic 2: the 2026 line only has data through August.
Graphic 3: NASA's gray "LSAT+SST Uncertainty" band is omitted because the downloadable CSV contains only the annual mean and Lowess columns.
Graphic 4: values are a few hundredths of a degree higher than in the NYT chart (2016 is +1.24 °C here vs about +1.22 °C) because NASA has revised GISTEMP v4 since 2019. The data is re-baselined from 1951-1980 to the 1880-1899 average and cut at 2018 to match the article.
AI Assistance

Prompts and outputs are logged in ai_documentation.txt.