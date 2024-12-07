import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup

def fetch_genomic_events():
    """Fetch genomic events (placeholder data)"""
    events = [
        {'Date': '2022-03-15', 'description': 'Moderna announces new mRNA vaccine trial'},
        {'Date': '2022-06-20', 'description': 'COVID-19 booster effectiveness study'},
        {'Date': '2022-09-10', 'description': 'New cancer vaccine development'},
        {'Date': '2023-01-25', 'description': 'RSV vaccine breakthrough'},
        {'Date': '2023-05-15', 'description': 'Phase 3 trial results announced'},
        {'Date': '2023-08-30', 'description': 'New mRNA platform technology'},
        {'Date': '2023-11-20', 'description': 'Flu vaccine emergency approval'},
        {'Date': '2024-01-15', 'description': 'Strategic partnership announcement'}
    ]
    return pd.DataFrame(events)

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch stock data using yfinance"""
    # Download the data
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    
    # Reset index to make Date a regular column
    stock_data = stock_data.reset_index()
    
    # Ensure column names are single-level
    stock_data.columns = [col[0] if isinstance(col, tuple) else col for col in stock_data.columns]
    
    # Ensure Date column is datetime
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    
    print(f"Fetched {len(stock_data)} days of stock data")
    return stock_data
