import joblib
import numpy as np

model = joblib.load("crop_recommendation_model.pkl")

# Sample input: [N, P, K, Temperature, Humidity, pH, Rainfall]
sample = np.array([[90, 42, 43, 20.87, 82.00, 6.5, 202.93]])

prediction = model.predict(sample)
print("Recommended Crop:", prediction[0])
