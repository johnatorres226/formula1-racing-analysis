# 🏎️ F1 2024 Data Science Project – Top 5 Drivers & Telemetry Analysis

This project aims to explore and analyze the 2024 Formula 1 season using telemetry data from the OpenF1 API, focusing on the **top five drivers** of the year and **car telemetry from Max Verstappen**. It lays the foundation for in-depth driver performance modeling, race strategy analysis, and interactive visualization based on structured and reproducible data.

---

## 🚦 Scope & Objectives

- 📆 Focus: **2024 Season Only**
- 🏁 Drivers:
  - Max Verstappen (🇳🇱 Red Bull)
  - Lando Norris (🇬🇧 McLaren)
  - Charles Leclerc (🇲🇨 Ferrari)
  - Oscar Piastri (🇦🇺 McLaren)
  - Carlos Sainz Jr. (🇪🇸 Ferrari)
- 🛠️ Dataset Types:
  - **Car Telemetry (car_data)** — Max Verstappen only
  - **Sessions, Laps, Positions, Stints, Race Control, Weather** — All top 5 drivers
- 📌 Goals:
  - Efficient API-based data acquisition and structured storage
  - Preparation of a clean and consistent 2024 race dataset
  - Enable future visualization, modeling, and driver performance research

---

## 📁 Project Structure
f1-2024-analysis/
├── data/
│ └── raw/
│ ├── car_data/
│ ├── laps/
│ ├── position/
│ ├── race_control/
│ ├── stints/
│ ├── weather/
│ ├── hybrid_sessions.csv
│ └── session_keys_2024.csv
├── notebooks/
│ └── 01_data_exploration.ipynb
├── utils/
│ └── api_handler.py
├── scripts/
│ └── download_car_data.py
│ └── download_metadata.py
├── README.md


---

## 🧰 Tools & Technologies

- Python 3.10+
- `requests`, `pandas`, `tqdm`
- OpenF1 API: https://www.openf1.org
- Jupyter Notebooks for analysis
- Git for version control

---

## 🧪 Phase 1: Data Acquisition & Preparation

### ✅ Tasks Completed

- [x] Created a utility handler (`api_handler.py`) to manage API latency and rate limits
- [x] Downloaded session metadata and filtered for 2024
- [x] Extracted `laps`, `position`, `stints`, `race_control`, `weather` for all 5 drivers
- [x] Downloaded **`car_data` only for Verstappen**
- [x] Logged missing/unavailable sessions for transparency

### 📦 Next Steps

- Store processed data in optimized formats (e.g., Parquet)
- Merge session metadata with telemetry and race control data
- Standardize time formats and align telemetry on lap timestamps

---

## 📊 Phase 2: Exploratory Dashboard *(Planned)*

**Goal**: Develop a lightweight dashboard for 2024 race analysis using:
- Plotly / Dash / Streamlit

**Visualizations:**
- Lap time trends
- Position deltas
- Tyre stint strategies
- Weather impact overlays

---

## 📈 Phase 3: Performance & Driving Style Analysis *(Planned)*

### 🔍 Telemetry Analysis
- Use Verstappen's car data to extract:
  - Throttle, brake, and steering traces
  - Sector-level pace breakdowns
  - Consistency across laps and stints

### 🔍 Driving Style Clustering
- Apply:
  - Dynamic Time Warping (DTW)
  - KMeans or Hidden Markov Models
- Purpose:
  - Identify dominant driving patterns
  - Compare early vs. late stint behavior

---

## 📌 Notes & Assumptions

- Only data for 2024 is processed.
- Driver number for Verstappen in 2024 is `1`, not `33`.
- Some sessions may not contain telemetry data and are skipped with logged status.
- API handler includes retry and latency logic to avoid rate-limit issues.

---

## 📂 Data Licensing & Attribution

All data is sourced from the [OpenF1 API](https://www.openf1.org), an open-source F1 telemetry and race event API. Ensure proper citation in any publications or public analyses using this dataset.

---

## 🏁 Author & Contact

**Project Lead**: *[Your Name]*  
Feel free to reach out for questions, collaboration, or contributions.
