import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Load columns
columns = pickle.load(open("columns.pkl", "rb"))

st.title("💳 Credit Card Fraud Detection")

st.write("Enter transaction details:")

# Create input fields dynamically
input_data = {}

for col in columns:
    input_data[col] = st.number_input(f"{col}", value=0.0)

# Scale the input data
scaler = StandardScaler()
input_data_scaled = scaler.fit_transform(pd.DataFrame([input_data]))

# Convert to DataFrame
input_df = pd.DataFrame([input_data_scaled.reshape(-1)], columns=columns)

# Prediction
if st.button("Predict"):
    prediction = model.predict(input_df)[0]

    if prediction == 1:
        st.error("🚨 Fraudulent Transaction Detected!")
    else:
        st.success("✅ Legitimate Transaction")