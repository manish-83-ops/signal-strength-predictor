import streamlit as st
import joblib
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Signal Predictor", layout="wide")


model = joblib.load("model.pkl")


st.title("📡 Wireless Signal Strength Predictor")
st.markdown("### Predict RSSI based on distance, frequency, and obstacles")


st.sidebar.header("⚙️ Input Parameters")

distance = st.sidebar.slider("Distance (meters)", 1, 200, 20)
frequency = st.sidebar.selectbox("Frequency (MHz)", [900, 1800, 2400])
obstacles = st.sidebar.slider("Obstacles", 0, 10, 2)


input_data = np.array([[distance, frequency, obstacles]])
prediction = model.predict(input_data)[0]


col1, col2 = st.columns(2)


with col1:
    st.subheader("📊 Prediction Result")

    st.metric(
        label="Signal Strength (dBm)",
        value=f"{prediction:.2f}"
    )

    
    if prediction > -60:
        st.success("🟢 Strong Signal")
    elif prediction > -80:
        st.warning("🟡 Moderate Signal")
    else:
        st.error("🔴 Weak Signal")


with col2:
    st.subheader("📉 Signal vs Distance")

    distances = np.linspace(1, 200, 50)
    preds = [model.predict([[d, frequency, obstacles]])[0] for d in distances]

    fig, ax = plt.subplots()
    ax.plot(distances, preds)
    ax.set_xlabel("Distance (m)")
    ax.set_ylabel("Signal Strength (dBm)")
    ax.set_title("Signal Decay Curve")

    st.pyplot(fig)


st.markdown("---")
st.markdown("Built with ❤️ using Machine Learning + Streamlit")