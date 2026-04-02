# F1 ML/DS — Race Prediction & Analysis

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastF1](https://img.shields.io/badge/FastF1-3.x-E10600?logo=f1&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

End-to-end data pipeline and machine learning project built on top of the official Formula 1 timing data. The goal is to predict race outcomes and analyze performance trends across seasons using real telemetry, results, and weather data.

---

## Features

- **ETL pipeline** — fetches race results, qualifying times, and session telemetry via FastF1
- **Weather integration** — pulls historical race-day weather from Open-Meteo
- **Local caching** — avoids redundant API calls with FastF1's built-in cache layer
- **Structured storage** — persists cleaned data to a relational database via SQLAlchemy
- **ML models** _(coming soon)_ — race position prediction, tire strategy analysis, qualifying pace modeling

---

## Project Structure

```
f1-ml-ds/
├── etl/
│   ├── fetch_f1,py        # FastF1 data ingestion (race & qualifying results)
│   └── cache/             # FastF1 local cache (git-ignored)
├── requirements.txt
└── README.md
```

---

## Setup

```bash
# 1. Create and activate a virtual environment
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate      # macOS / Linux

# 2. Install dependencies
pip install -r requirements.txt
```

---

## Usage

```python
from etl.fetch_f1 import fetch_race_results, fetch_qualifying_results

# Fetch full 2023 season race results
races = fetch_race_results(2023)

# Fetch full 2023 season qualifying results
quali = fetch_qualifying_results(2023)

print(races.head())
print(quali.head())
```

---

## Data Sources

| Source | Description |
|---|---|
| [FastF1](https://docs.fastf1.dev/) | Official F1 timing & telemetry data |
| [Open-Meteo](https://open-meteo.com/) | Historical weather for race locations |

---

## Roadmap

- [x] Race results ETL
- [x] Qualifying results ETL
- [ ] Weather data ETL
- [ ] Database schema & persistence layer
- [ ] Exploratory data analysis (EDA)
- [ ] Feature engineering
- [ ] Baseline ML models (race position prediction)
- [ ] Model evaluation & tuning

---

## License

MIT
