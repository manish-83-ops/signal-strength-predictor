import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib


df = pd.read_csv("signal_strength_dataset.csv")


X = df[['distance_m', 'frequency_MHz', 'obstacles']]
y = df['signal_strength_dBm']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)


joblib.dump(model, "model.pkl")

print("✅ Model trained and saved as model.pkl")


score = model.score(X_test, y_test)
print(f"Model R² Score: {score:.2f}")