#!/usr/bin/env python3
"""
TTC Data Ingestion Script

This script downloads and processes GTFS static schedule data from the TTC.
It extracts the ZIP file, validates the GTFS feed, and loads data into SQLite database.

Author: Matthew Sinaga
Date: 2024
"""

import os
import requests
import zipfile
import sqlite3
import pandas as pd
from pathlib import Path
from datetime import datetime
import logging

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Configuration
GTFS_URL = "https://ckan0.cf.opendata.inter.prod-toronto.ca/dataset/ttc-routes-and-schedules"
DATA_DIR = Path("data/raw/gtfs_static")
DB_PATH = Path("data/ttc_transit.db")

# GTFS Required Files
GTFS_FILES = [
    'agency.txt',
    'stops.txt',
    'routes.txt',
    'trips.txt',
    'stop_times.txt',
    'calendar.txt',
    'calendar_dates.txt'
]

def download_gtfs_data(url: str, output_path: Path) -> bool:
    """
    Download GTFS static data from TTC open data portal.
    
    Args:
        url: URL to download GTFS data
        output_path: Path to save the ZIP file
    
    Returns:
        bool: True if download successful, False otherwise
    """
    try:
        logger.info(f"Downloading GTFS data from {url}")
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        
        logger.info(f"Successfully downloaded GTFS data to {output_path}")
        return True
    
    except Exception as e:
        logger.error(f"Error downloading GTFS data: {e}")
        return False

def extract_gtfs_zip(zip_path: Path, extract_dir: Path) -> bool:
    """
    Extract GTFS ZIP file.
    
    Args:
        zip_path: Path to the ZIP file
        extract_dir: Directory to extract files to
    
    Returns:
        bool: True if extraction successful, False otherwise
    """
    try:
        logger.info(f"Extracting {zip_path} to {extract_dir}")
        extract_dir.mkdir(parents=True, exist_ok=True)
        
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_dir)
        
        logger.info("Extraction completed successfully")
        return True
    
    except Exception as e:
        logger.error(f"Error extracting ZIP file: {e}")
        return False

def validate_gtfs_files(gtfs_dir: Path) -> bool:
    """
    Validate that all required GTFS files exist.
    
    Args:
        gtfs_dir: Directory containing GTFS files
    
    Returns:
        bool: True if all required files exist, False otherwise
    """
    missing_files = []
    for file in GTFS_FILES:
        file_path = gtfs_dir / file
        if not file_path.exists():
            missing_files.append(file)
    
    if missing_files:
        logger.error(f"Missing required GTFS files: {missing_files}")
        return False
    
    logger.info("All required GTFS files present")
    return True

def load_gtfs_to_database(gtfs_dir: Path, db_path: Path) -> bool:
    """
    Load GTFS data into SQLite database.
    
    Args:
        gtfs_dir: Directory containing GTFS files
        db_path: Path to SQLite database
    
    Returns:
        bool: True if loading successful, False otherwise
    """
    try:
        logger.info("Loading GTFS data into database")
        db_path.parent.mkdir(parents=True, exist_ok=True)
        
        conn = sqlite3.connect(db_path)
        
        for file in GTFS_FILES:
            file_path = gtfs_dir / file
            table_name = file.replace('.txt', '')
            
            logger.info(f"Loading {file} into table {table_name}")
            df = pd.read_csv(file_path)
            df.to_sql(table_name, conn, if_exists='replace', index=False)
            
            logger.info(f"Loaded {len(df)} records from {file}")
        
        conn.close()
        logger.info("Successfully loaded all GTFS data into database")
        return True
    
    except Exception as e:
        logger.error(f"Error loading data to database: {e}")
        return False

def main():
    """
    Main execution function.
    """
    logger.info("Starting TTC GTFS data ingestion")
    
    # Create data directories
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    
    # Define file paths
    zip_path = DATA_DIR / "gtfs.zip"
    extract_dir = DATA_DIR
    
    # Note: Update GTFS_URL with the actual download link
    logger.info("Please manually download GTFS data from TTC Open Data portal")
    logger.info("URL: https://open.toronto.ca/dataset/ttc-routes-and-schedules/")
    
    # Check if ZIP file exists
    if not zip_path.exists():
        logger.warning(f"GTFS ZIP file not found at {zip_path}")
        logger.info("Please download the GTFS data manually and place it in the data/raw/gtfs_static directory")
        return
    
    # Extract GTFS data
    if not extract_gtfs_zip(zip_path, extract_dir):
        return
    
    # Validate GTFS files
    if not validate_gtfs_files(extract_dir):
        return
    
    # Load data into database
    if not load_gtfs_to_database(extract_dir, DB_PATH):
        return
    
    logger.info("TTC GTFS data ingestion completed successfully")

if __name__ == "__main__":
    main()
