# TTC Transit Punctuality Analysis

A comprehensive data analytics project analyzing Toronto Transit Commission (TTC) mobility patterns using GTFS static schedules and real-time vehicle position data.

![Project Status](https://img.shields.io/badge/status-active-success.svg)
![Python](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## 📊 Project Overview

This project provides a data-driven analysis of transit punctuality across Toronto's public transportation network, focusing on:

- **On-time performance** by route and mode (bus, streetcar, subway)
- **Headway adherence** and vehicle bunching detection
- **Service reliability** patterns by time of day and day of week
- **Stop-level analysis** identifying problematic corridors

### Key Deliverables

✅ **Interactive Tableau Dashboard** with 3 pages of visualizations  
✅ **Python ETL Pipeline** for automated data collection and processing  
✅ **SQLite Database** with optimized schema for transit analysis  
✅ **Comprehensive Documentation** including setup guides and data dictionary

---

## 🎯 Research Questions

1. What is the on-time performance of TTC routes by mode?
2. Which corridors and stops experience the worst delays?
3. Where and when does vehicle bunching occur?
4. How does punctuality vary by time of day and day of week?
5. What is the headway adherence for high-frequency routes?

---

## 📁 Project Structure

```
ttc-transit-punctuality/
├── data/
│   ├── raw/gtfs_static/       # Downloaded GTFS files
│   ├── processed/              # Cleaned data
│   └── tableau_export/         # CSV exports for Tableau
├── scripts/
│   ├── ttc_data_ingestion.py           # Main ETL pipeline
│   ├── collect_realtime_continuous.py  # Real-time collector
│   └── export_for_tableau.py           # Tableau export
├── dashboards/
│   └── TTC_Punctuality.twbx    # Tableau workbook
├── docs/
│   ├── TTC-Project-Summary.pdf
│   ├── TABLEAU_SETUP_GUIDE.md
│   └── DATA_DICTIONARY.md
├── ttc_transit_analysis.db      # SQLite database
├── requirements.txt
├── .gitignore
├── LICENSE
└── README.md
```

---

## 🗂️ Data Sources

### GTFS Static Data
- **Source**: [Toronto Open Data Portal](http://opendata.toronto.ca/toronto.transit.commission/ttc-routes-and-schedules/TTC_GTFS.zip)
- **Size**: 62-78 MB per snapshot
- **Update**: Monthly
- **Contents**: 200 routes, 12,000 stops, 2-3M scheduled stop times

### GTFS Real-time Data
- **Source**: TTC BusTime API
- **Format**: XML feed
- **Poll Frequency**: Every 30 seconds
- **Daily Volume**: 100,000-200,000 position records
- **Recommendation**: Collect 1-2 weeks for comprehensive analysis

---

## 🚀 Getting Started

### Prerequisites

```bash
python --version  # Python 3.9+
pip install -r requirements.txt
```

### Installation

```bash
# Clone the repository
git clone https://github.com/mlcsinaga/ttc-transit-punctuality.git
cd ttc-transit-punctuality

# Install dependencies
pip install -r requirements.txt
```

### Usage

#### Step 1: Download GTFS Static Data
```bash
python scripts/ttc_data_ingestion.py
```

#### Step 2: Collect Real-time Data (run for 7-14 days)
```bash
python scripts/collect_realtime_continuous.py
```

#### Step 3: Export for Tableau
```bash
python scripts/export_for_tableau.py
```

#### Step 4: Build Dashboard
Open Tableau Public/Desktop and import the 6 CSV files from `data/tableau_export/`

See [TABLEAU_SETUP_GUIDE.md](docs/TABLEAU_SETUP_GUIDE.md) for detailed instructions.

---

## 📈 Key Performance Indicators

### On-Time Performance
**Definition**: Arrivals within -1 to +5 minutes of schedule  
**Formula**: `(On-Time Arrivals / Total Arrivals) × 100`

**Benchmarks**:
- 🟢 Excellent: ≥90%
- 🟡 Good: 80-89%
- 🟠 Fair: 70-79%
- 🔴 Poor: <70%

### Headway Adherence
**Definition**: Actual vehicle spacing vs scheduled  
**Bunching**: When actual headway < 50% of scheduled

### Reliability Score
**Composite Metric**: `On-Time % - (Delay Std Dev / 2)`

---

## 📊 Dashboard Pages

### 1. Route Scorecard
- Overall on-time performance by route
- Performance heatmap by hour of day
- Daily trend lines
- KPI cards (Total Routes, On-Time %, Avg Delay, Bunching Rate)

### 2. Bunching Heatmap
- Geographic map of bunching hotspots
- Route × hour heatmap
- Headway distribution (scheduled vs actual)

### 3. Stop-Level Reliability
- Individual stop performance map
- Top 20 worst-performing stops
- Reliability by day of week

---

## 💡 Sample Insights

### High-Performing Routes
- 🚇 Subway lines: 85-92% on-time
- 🚌 Off-peak bus routes: 75-80% on-time

### Problem Areas
- 🚊 King St (504) & Queen St (501) streetcars: frequent bunching
- ⏰ PM rush hour (4-6 PM): worst system-wide performance
- 🔄 Major transfer points: Bloor-Yonge, St George

### Time Patterns
- ✅ Best: Early morning (5-7 AM), late evening (9 PM-midnight)
- ❌ Worst: PM rush hour (especially 4:30-6 PM)
- 📅 Weekend: 10-15% better than weekdays

---

## 🛠️ Technical Stack

- **Python 3.9+**: pandas, requests, sqlite3
- **SQLite**: Database storage
- **Tableau Public**: Interactive dashboards
- **GTFS**: Industry-standard transit data format

---

## 💼 Business Value

### For Transit Planners
- Identify underperforming routes requiring intervention
- Optimize service frequency based on actual demand
- Prioritize infrastructure investments

### For TTC Operations
- Real-time service quality monitoring
- Proactive bunching detection and response
- Performance benchmarking

### For Riders
- Transparent performance data
- Route comparison for informed choices
- Advocacy tool for transit improvements

---

## 📚 Documentation

- [Project Summary PDF](docs/TTC-Project-Summary.pdf) - Comprehensive project overview
- [Tableau Setup Guide](docs/TABLEAU_SETUP_GUIDE.md) - Dashboard creation instructions
- [Data Dictionary](docs/DATA_DICTIONARY.md) - Field definitions and schemas

---

## 🔮 Future Enhancements

### Short-term
- Integrate GTFS-RT trip updates for predicted arrivals
- Service alerts integration
- Automated weekly reporting

### Medium-term
- Historical year-over-year comparisons
- Weather correlation analysis
- Route optimization recommendations

### Long-term
- Predictive ML models for delay forecasting
- Real-time route recommendations
- Mobile app for riders

---

## 🎓 Skills Demonstrated

**Data Engineering**: ETL pipeline, API integration, database design  
**Data Analysis**: Geospatial analysis, time-series, statistical analysis, KPI development  
**Data Visualization**: Tableau dashboards, interactive filtering, geographic mapping  
**Technical Skills**: Python, SQL, GTFS standards, XML parsing, Git/GitHub

---

## 🔗 Links

- **GitHub**: [github.com/mlcsinaga/ttc-transit-punctuality](https://github.com/mlcsinaga/ttc-transit-punctuality)
- **Tableau Public**: [public.tableau.com/profile/matthewsinaga](https://public.tableau.com/profile/matthewsinaga)
- **Portfolio**: [mattsinaga.com](https://mattsinaga.com)
- **LinkedIn**: [linkedin.com/in/matthewsinaga](https://linkedin.com/in/matthewsinaga)

---

## 👤 Author

**Matthew Sinaga**  
Data Analyst | Full-Stack Developer  
Toronto, ON

📧 mlcsinaga@gmail.com  
💼 [@mlcsinaga](https://github.com/mlcsinaga)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

**Data Sources**: TTC GTFS data © Toronto Transit Commission, available under Toronto Open Data License.

---

## 🙏 Acknowledgments

- Toronto Transit Commission for open GTFS data
- City of Toronto Open Data Team
- Transitland for GTFS-RT services
- GTFS Community for standardized formats

---

**⭐ If you find this project helpful, please star it on GitHub!**
