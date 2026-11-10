GridWise AU

An open-source learning project exploring Australian electricity market data, wholesale price trends, and future forecasting.

📖 Project Overview

GridWise AU is a Python-based data analysis project focused on understanding electricity demand and wholesale electricity prices in Australia's National Electricity Market (NEM).

The project currently focuses on New South Wales (NSW1) using historical electricity market data published by the Australian Energy Market Operator (AEMO).

The main goals are to:

Understand how electricity demand and wholesale prices change over time.

Explore the relationship between electricity demand and wholesale electricity prices.

Identify patterns across different months, seasons, and times of day.

Develop practical skills in Python, SQL, data analysis, and visualisation.

Eventually build simple forecasting models and an interactive dashboard.

Note: Wholesale electricity prices are different from the retail electricity tariffs paid by households.

🛠️ Technologies Used

Technology

Purpose

Python

Data collection, processing, and analysis

Pandas

Working with CSV files and calculating statistics

Matplotlib

Creating charts and visualisations

Requests

Downloading historical electricity data

Git

Tracking changes to the project

GitHub

Hosting and sharing the project

Planned Technologies

PostgreSQL: Store and query historical electricity market data.

DataGrip: Write SQL queries and manage the PostgreSQL database.

Streamlit: Build an interactive electricity market dashboard.

Scikit-learn: Explore beginner-friendly electricity demand and price-risk forecasting.

Power BI: Create additional data visualisations (optional).

These tools are part of the future roadmap and have not yet been integrated into GridWise AU.

📊 Dataset

Source: Australian Energy Market Operator (AEMO)

Dataset: Price and Demand

Region: NSW1 — New South Wales

Historical period analysed: October 2023 to September 2026

The three-year dataset contains:

36 months of historical records.

315,648 five-minute observations.

Electricity demand measured in megawatts (MW).

Wholesale electricity prices measured in Australian dollars per megawatt-hour (AUD/MWh).

The original data comes from:

AEMO Price and Demand Data

Large downloaded and processed datasets are excluded from the Git repository. Python scripts are provided to reproduce the analysis.

✅ Completed Work

1. Data Collection

Created Python scripts to download historical NSW electricity market data from AEMO.

2. Data Validation

Checked for missing values, duplicate timestamps, and irregular five-minute intervals to help ensure the dataset is suitable for analysis.

3. Electricity Market Visualisation

Created charts showing historical NSW electricity demand and wholesale electricity prices.

4. Demand and Price Correlation

Investigated whether higher electricity demand tends to occur alongside higher wholesale electricity prices.

For September 2026, the hourly demand–price Pearson correlation was approximately +0.738, indicating a strong positive linear relationship during that month.

5. Three-Year Correlation Analysis

Expanded the analysis to 36 months, examining how the relationship changes over time.

Key observations:

All 36 months showed positive demand–price correlations.

The strongest monthly correlation was approximately +0.787 in October 2023.

The weakest monthly correlation was approximately +0.156 in May 2024.

Correlation strengths varied substantially across months.

Correlations calculated across complete years were generally weaker than those observed in some individual months.

These findings suggest that demand alone cannot fully explain wholesale electricity price movements.

6. Hour-of-Day Analysis

Calculated average electricity demand and wholesale prices for each hour of the day using three years of historical data.

Key observations:

Highest average wholesale price: $278.68/MWh, between 5 PM and 6 PM.

Highest average electricity demand: 9,407 MW, between 6 PM and 7 PM.

Lowest average wholesale price: $35.38/MWh, between 10 AM and 11 AM.

The results show a pronounced evening peak in average wholesale prices.

These are historical averages, not forecasts. Correlation also does not establish causation.

📈 Visualisations

The project currently includes charts such as:

NSW wholesale electricity prices during September 2026.

NSW electricity demand during September 2026.

NSW electricity demand versus wholesale price.

Monthly demand–price correlations across three years.

Average NSW wholesale electricity prices by hour of day.

Generated charts are stored in outputs/charts/.

📁 Project Structure

gridwise-au/
├── src/
│   ├── fetch_aemo.py
│   ├── check_aemo_data.py
│   ├── plot_aemo.py
│   ├── demand_vs_price.py
│   ├── download_36_months.py
│   ├── monthly_correlations.py
│   └── hour_of_day.py
├── data/
│   ├── raw/
│   └── processed/
├── outputs/
│   ├── charts/
│   └── tables/
├── .gitignore
└── README.md

Folder descriptions:

src/ — Python scripts used for data collection and analysis.

data/raw/ — Original downloaded AEMO data.

data/processed/ — Combined and prepared datasets.

outputs/charts/ — Generated graphs and visualisations.

outputs/tables/ — CSV summaries of analysis results.

🚀 Getting Started

1. Clone the repository

git clone https://github.com/jchoi130/gridwise-au.git
cd gridwise-au

2. Create a Python virtual environment

On Windows:

py -m venv .venv

3. Install the required Python libraries

.\.venv\Scripts\python.exe -m pip install pandas matplotlib requests

4. Download and prepare the historical dataset

.\.venv\Scripts\python.exe src\download_36_months.py

This script downloads and validates the historical AEMO records, then creates the processed three-year dataset.

5. Run the analysis

For monthly correlations:

.\.venv\Scripts\python.exe src\monthly_correlations.py

For hourly electricity prices:

.\.venv\Scripts\python.exe src\hour_of_day.py

Results are displayed in the terminal, with relevant charts and tables saved in the outputs/ directory.

🗺️ Project Roadmap

Download historical electricity market data.

Validate and clean data.

Visualise demand and wholesale electricity prices.

Investigate demand–price correlations.

Analyse three years of NSW electricity market data.

Explore hourly electricity price patterns.

Set up PostgreSQL and connect using DataGrip.

Learn and apply SQL queries to electricity data.

Connect Python to PostgreSQL.

Build an interactive Streamlit dashboard.

Investigate additional factors affecting electricity prices.

Develop and evaluate introductory forecasting models.

🎯 Project Purpose

GridWise AU is both a personal learning project and an effort to make Australian electricity market data easier to explore and understand.

The project is being developed incrementally, with a focus on clear code, reproducible analysis, and practical learning.

The long-term goal is to create an accessible platform for understanding electricity market behaviour and investigating how wholesale market conditions relate to broader electricity costs.

⚠️ Disclaimer

GridWise AU is an educational and exploratory project.

Its analysis uses historical market data and should not be treated as financial advice, retail electricity pricing guidance, or a reliable prediction of future electricity costs.

Electricity market conditions are influenced by many factors, and historical relationships do not guarantee future outcomes.

GridWise AU — Understanding Australia's electricity market, one dataset at a time. ⚡