# visualization.py

import matplotlib.pyplot as plt

def plot_events_on_stock(merged_data):
    """Plot stock prices with genomic events"""
    plt.figure(figsize=(20,10))
    
    # Plot stock price
    plt.plot(merged_data['Date'], merged_data['Close'], label='MRNA Stock Price', color='blue')
    
    # Plot events
    events = merged_data[merged_data['has_event'] == 1]
    for _, event in events.iterrows():
        # Add vertical line for event
        plt.axvline(event['Date'], color='red', alpha=0.3, linestyle='--')
        
        # Add event marker
        plt.plot(event['Date'], event['Close'], 'ro', markersize=10)
        
        # Add annotation with event description
        plt.annotate(event['description'], 
                    xy=(event['Date'], event['Close']),
                    xytext=(10, 20), textcoords='offset points',
                    bbox=dict(facecolor='white', edgecolor='red', alpha=0.7),
                    fontsize=9,
                    arrowprops=dict(arrowstyle='->'))
    
    plt.title('Moderna (MRNA) Stock Price with Major Genomic Events', fontsize=14, pad=20)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Stock Price ($)', fontsize=12)
    plt.grid(True, alpha=0.3)
    plt.legend(fontsize=10)
    
    # Rotate x-axis dates for better readability
    plt.xticks(rotation=45)
    
    # Adjust layout to prevent label cutoff
    plt.tight_layout()
    
    # Save and show plot
    plt.savefig('moderna_stock_events.png', dpi=300, bbox_inches='tight')
    print("Plot saved as 'moderna_stock_events.png'")
    plt.show(block=True)
