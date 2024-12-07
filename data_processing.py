# data_processing.py

import pandas as pd
import nltk

def process_genomic_events(genomic_events_df):
    """Process genomic events data."""
    if genomic_events_df.empty:
        print("Warning: Empty genomic events DataFrame")
        return genomic_events_df
        
    try:
        # Simplified processing - just clean up the text
        genomic_events_df['description'] = genomic_events_df['description'].fillna('')
        genomic_events_df['summary'] = genomic_events_df['summary'].fillna('')
        
        # Combine title and summary
        genomic_events_df['full_text'] = genomic_events_df['description'] + ' ' + genomic_events_df['summary']
        
        print(f"Processed {len(genomic_events_df)} genomic events")
    except Exception as e:
        print(f"Error processing genomic events: {e}")
    
    return genomic_events_df

def merge_data(stock_data, genomic_events):
    """Merge stock data with genomic events"""
    stock_data['Date'] = pd.to_datetime(stock_data['Date'])
    genomic_events['Date'] = pd.to_datetime(genomic_events['Date'])
    
    merged_data = pd.merge(stock_data, genomic_events, on='Date', how='left')
    merged_data['has_event'] = merged_data['description'].notna().astype(int)
    
    return merged_data

