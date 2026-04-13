import streamlit as st
import joblib
import numpy as np
import plotly.express as px
import pandas as pd

# Load your trained models
@st.cache_resource
def load_models():
    xgb_model = joblib.load('xgb_model.pkl')
    le = joblib.load('label_encoder.pkl')
    return xgb_model, le

st.set_page_config(page_title="Crop Advisor Pro", page_icon="🌾", layout="wide")

# Header
st.title("🌾 Precision Crop Advisor Pro")
st.markdown("**99.5% XGBoost • Senthoor-Mani • SRM BCA 2026**")
st.markdown("---")

# City presets (Maharashtra)
cities = {
    "Pune (Fertile)": [90, 42, 43, 21, 82, 6.5, 203],
    "Nagpur (Dry)": [60, 50, 40, 25, 65, 7.2, 150],
    "Aurangabad (Poor Soil)":
