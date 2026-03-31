# 📡 Signal Predictor (Wireless Signal Strength Estimator)

🔗 **Live Demo:** https://share.google/BcfmFj4lJxqN9aN6T

##  Project Overview

Signal Predictor is a Machine Learning web application that estimates **wireless signal strength (RSSI in dBm)** based on:

- Distance between transmitter and receiver  
- Operating frequency (MHz)  
- Number of obstacles in the environment  

It uses a **Random Forest Regressor** trained on synthetic/realistic signal propagation data and provides an interactive UI built with **Streamlit**.

---

## 🎯 Features

- 📊 Real-time signal strength prediction  
- 📡 Adjustable input parameters via sidebar sliders  
- 🟢 Signal quality classification (Strong / Moderate / Weak)  
- 📉 Visual signal decay curve vs distance  
- ⚡ Fast ML inference using trained Random Forest model  
- 🌐 Interactive and responsive Streamlit web app  

---

## 🧠 Tech Stack

- Python   
- Pandas  
- NumPy  
- Scikit-learn (Random Forest Regressor)  
- Matplotlib  
- Streamlit  
- Joblib (model serialization)

---

## 📂 Project Structure
signal-strength-predictor/ │ ├── app.py                 # Streamlit web app ├── training.py            # Model training script ├── model.pkl              # Saved ML model ├── signal_strength_dataset.csv └── README.md

---

## ⚙️ How It Works

1. Dataset is loaded (`signal_strength_dataset.csv`)
2. Features used:
   - Distance (meters)
   - Frequency (MHz)
   - Obstacles count
3. Model trained using **Random Forest Regressor**
4. Saved using `joblib`
5. Streamlit app loads model and performs live predictions

---

## 📈 Model Performance

- Model: Random Forest Regressor  
- Metric: R² Score (printed after training)  
- Goal: Capture nonlinear signal attenuation patterns

---

## ▶️ Run Locally

```bash
# Clone repository
git clone https://github.com/your-username/signal-strength-predictor.git

# Move into folder
cd signal-strength-predictor

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py

📌 Future Improvements
Add terrain + weather factors 🌦️
Replace Random Forest with XGBoost or Neural Network
Deploy on Streamlit Cloud permanently
Add 3D visualization of signal coverage
Export prediction reports