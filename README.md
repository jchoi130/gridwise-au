# gridwise-au
Open-source Australian electricity market intelligence and forecasting platform
GridWise AU

Australian Electricity Market Intelligence & Forecasting

🚧 Work in Progress — Currently in Early Development

GridWise AU is an open-source machine learning project focused on analysing, visualising, and forecasting Australia's electricity market using publicly available data.

The project aims to make electricity market information more accessible, transparent, and understandable for Australians.

🎯 Project Objectives

Electricity Price Forecasting: Explore machine learning models to forecast wholesale electricity prices across Australia's National Electricity Market (NEM).

Energy Demand Analysis: Identify historical consumption patterns, seasonal trends, and peak demand periods.

Market Insights: Visualise electricity price fluctuations, demand trends, and regional market differences.

Explainable Predictions: Investigate the factors influencing electricity prices and demand.

Accessible Dashboard: Develop a free, interactive web dashboard for exploring electricity market data.

📊 Data Sources

The project will primarily use publicly available Australian datasets, including:

Australian Energy Market Operator (AEMO) — Wholesale electricity prices, demand, and market data.

Australian Bureau of Statistics (ABS) — Relevant Australian economic and demographic statistics.

Bureau of Meteorology (BoM) — Weather and climate data, subject to access and licensing requirements.

🛠️ Proposed Technology Stack

Python — Data processing and analysis

Pandas / NumPy — Data manipulation

Scikit-learn — Machine learning and forecasting

React / TypeScript — Interactive dashboard

GitHub Actions — Automated data processing

GitHub Pages — Free static website hosting

Technologies may change as development progresses.

🗺️ Development Roadmap

Phase 1 — Data collection and exploratory analysis

Phase 2 — Historical electricity market visualisation

Phase 3 — Electricity price and demand forecasting

Phase 4 — Model evaluation and explainability

Phase 5 — Interactive web dashboard

Phase 6 — Public deployment and documentation

🌏 Project Vision

To build a free, accessible, and data-driven platform that helps Australians better understand electricity market trends and supports informed energy-related decisions.

Note: Wholesale electricity prices are not equivalent to household retail electricity tariffs. Forecasts and insights will be indicative, not personalised electricity bill predictions.

Status: 🚧 Early Development

Focus: Machine Learning · Time Series Forecasting · Energy Analytics · Open Data · Australia

Further updates will be published as development progresses.


ok mate do you think we should add this to github at this stage?
Absolutely, mate! 🔥 I think we should push GridWise AU to GitHub now.

We've achieved enough to show that this is a genuine data science project, not just an idea in a README.

What we've accomplished
Milestone

Status

Downloaded real AEMO electricity data

 Complete

Validated 8,640 records

 Complete

Created price and demand charts

 Complete

Created demand-versus-price scatter plot

 Complete

Measured Pearson correlation: +0.738

 Complete

Publish the first milestone to GitHub

Next

Step 1 — Update your README
Open README.md in VS Code and add this section below your existing project description.

## Current Progress

### Phase 1 — NSW Electricity Market Analysis

Completed:
- Downloaded September 2026 NSW electricity market data from AEMO.
- Validated 8,640 five-minute observations.
- Checked missing values, duplicate timestamps and time gaps.
- Visualised wholesale electricity prices and demand.
- Analysed the relationship between electricity demand and wholesale prices.

### Initial Findings

Using 720 hourly observations from September 2026:

- Pearson correlation between demand and price: **+0.738**
- Higher-demand hours generally coincided with higher wholesale prices.
- Wholesale prices also varied substantially at similar demand levels.

These are preliminary findings from one month of data. Correlation does not establish causation.

### Next Steps

- Expand historical data collection to three years.
- Investigate seasonal patterns.
- Incorporate weather and generation data.
- Develop machine learning forecasting models.