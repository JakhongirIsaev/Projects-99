# main.py

from data_collection import fetch_genomic_events, fetch_stock_data
from data_processing import merge_data
from visualization import plot_events_on_stock

def main():
    # Parameters
    ticker = 'MRNA'  # Moderna
    start_date = '2022-01-01'  # Extended to 2 years
    end_date = '2024-03-01'

    print("\n1. Fetching stock data...")
    stock_data = fetch_stock_data(ticker, start_date, end_date)
    
    print("\n2. Fetching genomic events...")
    genomic_events = fetch_genomic_events()
    print(f"Found {len(genomic_events)} genomic events")

    print("\n3. Merging data...")
    merged_data = merge_data(stock_data, genomic_events)
    print(f"Merged data shape: {merged_data.shape}")

    print("\n4. Creating visualization...")
    plot_events_on_stock(merged_data)
    print("Done!")

if __name__ == "__main__":
    main()


