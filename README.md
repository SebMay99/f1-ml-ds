# F1 Podium Predictor

![Python](https://img.shields.io/badge/Python-3.11%2B-3776AB?logo=python&logoColor=white)
![FastF1](https://img.shields.io/badge/FastF1-3.x-E10600?logo=f1&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.x-150458?logo=pandas&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-ORM-D71F00)
![Status](https://img.shields.io/badge/Status-In%20Progress-yellow)
![License](https://img.shields.io/badge/License-MIT-green)

End-to-end machine learning project that predicts Formula 1 race podiums. Built on real F1 timing data and race-day weather, with a full pipeline from ETL to a React frontend served by a FastAPI backend.

---

## Architecture

```
f1-podium-predictor/
│
├── data/
│   ├── raw/                    # Cached API responses
│   └── processed/              # Cleaned, feature-ready data
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_feature_engineering.ipynb
│   └── 03_model_training.ipynb
│
├── etl/
│   ├── fetch_f1.py             ✅ F1 results & qualifying via FastF1
│   ├── fetch_weather.py        ✅ Race-day weather via Open-Meteo
│   └── pipeline.py             ← in progress
│
├── ml/
│   ├── features.py
│   ├── train.py
│   └── predict.py
│
├── api/
│   ├── main.py
│   └── routes/
│
├── frontend/
│
├── models/
├── requirements.txt
├── README.md
└── docker-compose.yml
```

---

## Sprints

| # | Goal | Status |
|---|------|--------|
| 1 | ETL — F1 results + weather into SQLite | In progress |
| 2 | Feature engineering + XGBoost baseline | Pending |
| 3 | Evaluation, neural network, model serialization | Pending |
| 4 | FastAPI with `/predict` endpoint | Pending |
| 5 | React frontend — race selector → predicted podium | Pending |
| 6 | Deploy on Railway + final README + LinkedIn post | Pending |

---

## Setup

```bash
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate      # macOS / Linux

pip install -r requirements.txt
```

---

## Usage

```python
from etl.fetch_f1 import fetch_race_results, fetch_qualifying_results
from etl.fetch_weather import fetch_race_weather

# Fetch 2023 season
races = fetch_race_results(2023)
quali  = fetch_qualifying_results(2023)

# Fetch weather for a specific race location and date
weather = fetch_race_weather(lat=51.5, lon=-1.7, date="2023-07-09")
```

---

## Data Sources

| Source | Description |
|--------|-------------|
| [FastF1](https://docs.fastf1.dev/) | Official F1 timing, telemetry & session results |
| [Open-Meteo](https://open-meteo.com/) | Historical race-day weather (free, no API key) |

---

## License

MIT
