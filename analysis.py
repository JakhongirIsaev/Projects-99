# analysis.py

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, r2_score
import pandas as pd

def prepare_features(data):
    """Prepare features and target variable for modeling."""
    if data.empty:
        print("Warning: Empty data provided for feature preparation")
        return None, None
        
    try:
        # Calculate returns for different periods
        data['Return'] = data['Close'].pct_change()
        data['Return_1d'] = data['Return'].shift(-1)  # Next day's return
        data['Return_5d'] = data['Close'].pct_change(periods=5).shift(-5)  # 5-day future return
        
        # Create features
        features = pd.DataFrame()
        features['Event_Occurred'] = data['Event_Occurred']
        features['Price_Momentum'] = data['Close'].pct_change(5)  # 5-day historical momentum
        features['Volume_Change'] = data['Volume'].pct_change()
        
        # Target variable (next day's return)
        target = data['Return_1d']
        
        # Remove rows with NaN values
        valid_idx = ~(features.isna().any(axis=1) | target.isna())
        features = features[valid_idx]
        target = target[valid_idx]
        
        print(f"Prepared {len(features)} samples for analysis")
        print("Feature statistics:")
        print(features.describe())
        
        return features, target
    except Exception as e:
        print(f"Error preparing features: {e}")
        return None, None

def train_model(X, y):
    """Train a Random Forest model."""
    if X is None or y is None:
        print("Warning: No valid data for training")
        return None
        
    try:
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, shuffle=False)
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        mae = mean_absolute_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        
        print(f"Model Performance:")
        print(f"Mean Absolute Error: {mae:.4f}")
        print(f"R^2 Score: {r2:.4f}")
        
        return model
    except Exception as e:
        print(f"Error training model: {e}")
        return None
