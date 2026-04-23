import streamlit as st
import pandas as pd
import joblib

# Load model + encoder
model = joblib.load("crop_model.pkl")
le = joblib.load("label_encoder.pkl")

st.set_page_config(page_title="Crop Recommendation", layout="centered")

st.markdown("<h2 style='text-align:center;'>🌱 Crop Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;color:gray;'>Enter soil and environmental conditions</p>", unsafe_allow_html=True)

st.divider()

# ---------- INPUTS ----------
st.subheader("🌾 Soil Nutrients")
col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 150, 50)

with col2:
    P = st.number_input("Phosphorus (P)", 0, 150, 50)

with col3:
    K = st.number_input("Potassium (K)", 0, 250, 50)

st.subheader("🌦️ Environmental Conditions")
col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 70.0)

with col2:
    ph = st.number_input("Soil pH", 0.0, 14.0, 6.5)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

st.divider()

# ---------- PREDICT ----------
if st.button("🌿 Recommend Crop", use_container_width=True):

    input_data = pd.DataFrame([[
        N, P, K, temperature, humidity, ph, rainfall
    ]], columns=[
        "N","P","K","temperature","humidity","ph","rainfall"
    ])

    probs = model.predict_proba(input_data)[0]

    # Top 3 crops
    top3_idx = probs.argsort()[-3:][::-1]
    crops = le.inverse_transform(top3_idx)
    scores = probs[top3_idx]

    st.subheader("🌱 Recommended Crops")

    for i in range(3):
        st.write(f"{i+1}. **{crops[i].upper()}** ({scores[i]*100:.2f}%)")