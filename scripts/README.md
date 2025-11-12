# TTC Transit Punctuality Analysis - Scripts

This directory contains Python scripts for the TTC Transit Punctuality Analysis project.

## Scripts Overview

### 1. ttc_data_ingestion.py
**Purpose:** Downloads and processes GTFS static schedule data from TTC.

**Features:**
- Downloads GTFS ZIP files from TTC Open Data portal
- Extracts and validates GTFS feed files
- Loads data into SQLite database
- Handles all required GTFS files (agency, stops, routes, trips, stop_times, calendar)

**Usage:**
```bash
python ttc_data_ingestion.py
```

### 2. collect_realtime_continuous.py  
**Purpose:** Continuously collects real-time vehicle position data from TTC GTFS-RT feed.

**Features:**
- Connects to TTC GTFS Realtime API
- Polls vehicle positions at configured intervals
- Parses GTFS-RT protobuf messages
- Stores real-time data in SQLite database
- Runs as a continuous background process

**Usage:**
```bash
python collect_realtime_continuous.py
```

### 3. compute_punctuality_metrics.py
**Purpose:** Calculates punctuality metrics by comparing scheduled vs. actual arrival times.

**Features:**
- Matches real-time positions with scheduled stop times
- Calculates delay/early arrival metrics
- Computes on-time performance (OTP) percentages
- Calculates headway adherence
- Generates reliability scores by route, time period, and day of week

**Usage:**
```bash
python compute_punctuality_metrics.py
```

### 4. export_for_tableau.py
**Purpose:** Exports processed data in formats optimized for Tableau visualization.

**Features:**
- Queries aggregated punctuality metrics from database
- Formats data for Tableau consumption
- Exports to CSV files
- Creates separate exports for different dashboard pages

**Usage:**
```bash
python export_for_tableau.py
```

## Data Flow

```
1. ttc_data_ingestion.py → Loads GTFS static data into database
2. collect_realtime_continuous.py → Continuously collects real-time vehicle positions
3. compute_punctuality_metrics.py → Processes data and calculates metrics
4. export_for_tableau.py → Exports data for visualization
```

## Requirements

All dependencies are listed in the root `requirements.txt` file. Install with:

```bash
pip install -r requirements.txt
```

## Configuration

Scripts use environment variables and configuration files located in the project root:
- Database path: `data/ttc_transit.db`
- GTFS static data: `data/raw/gtfs_static/`
- Processed data: `data/processed/`
- Tableau exports: `data/tableau_export/`

## Logging

All scripts use Python's `logging` module with INFO level by default. Logs include:
- Timestamp
- Script name
- Log level
- Message

## Error Handling

Scripts implement comprehensive error handling:
- Network errors with retry logic
- Data validation checks
- Database connection management
- Graceful degradation on partial failures
