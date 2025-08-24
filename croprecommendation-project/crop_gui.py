import tkinter as tk
from tkinter import messagebox
import numpy as np
import joblib

# Load model
model = joblib.load("crop_recommendation_model.pkl")

# GUI Function
def recommend_crop():
    try:
        # Get values from input fields
        N = float(entry_N.get())
        P = float(entry_P.get())
        K = float(entry_K.get())
        temp = float(entry_temp.get())
        humidity = float(entry_humidity.get())
        ph = float(entry_ph.get())
        rainfall = float(entry_rainfall.get())

        # Create input array
        sample = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        prediction = model.predict(sample)
        result_label.config(text=f"✅ Recommended Crop: {prediction[0]}")
    except Exception as e:
        messagebox.showerror("Error", f"Invalid input: {e}")

# Create window
root = tk.Tk()
root.title("🌾 Crop Recommendation System")
root.geometry("400x500")
root.configure(bg="#e6f2ff")

# Title Label
tk.Label(root, text="Enter Soil & Climate Details", font=("Arial", 16, "bold"), bg="#e6f2ff").pack(pady=10)

# Input fields
def create_input(label_text):
    tk.Label(root, text=label_text, font=("Arial", 12), bg="#e6f2ff").pack()
    entry = tk.Entry(root, font=("Arial", 12))
    entry.pack(pady=5)
    return entry

entry_N = create_input("Nitrogen (N)")
entry_P = create_input("Phosphorus (P)")
entry_K = create_input("Potassium (K)")
entry_temp = create_input("Temperature (°C)")
entry_humidity = create_input("Humidity (%)")
entry_ph = create_input("pH")
entry_rainfall = create_input("Rainfall (mm)")

# Predict Button
tk.Button(root, text="Recommend Crop", command=recommend_crop, bg="#4CAF50", fg="white", font=("Arial", 12, "bold")).pack(pady=15)

# Result Label
result_label = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#333", bg="#e6f2ff")
result_label.pack(pady=20)

# Run the GUI
root.mainloop()
