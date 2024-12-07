import requests
from bs4 import BeautifulSoup
import pandas as pd

def fetch_genomic_events():
    """Scrape genomic events directly from GenomeWeb."""
    url = "https://www.genomeweb.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    events = []
    for article in soup.find_all("article"):
        title = article.find("h2").text.strip()
        date = article.find("time")['datetime'] if article.find("time") else None
        events.append({"date": date, "description": title})

    # Convert to DataFrame
    genomic_events = pd.DataFrame(events)
    genomic_events['date'] = pd.to_datetime(genomic_events['date'], errors='coerce')
    genomic_events.dropna(subset=['date'], inplace=True)
    return genomic_events


import yfinance as yf

def fetch_stock_data(ticker, start_date, end_date):
    """Fetch historical stock data using yfinance."""
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    return stock_data


def merge_data(stock_data, genomic_events):
    """Merge stock data with genomic events dynamically."""
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    genomic_events['date'] = pd.to_datetime(genomic_events['date'])
    merged_data = pd.merge(stock_data, genomic_events, left_on='Date', right_on='date', how='left')
    return merged_data
