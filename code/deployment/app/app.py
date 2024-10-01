# app.py
import streamlit as st
import requests
import pandas as pd

st.title('Wine Classifier')

# Define input fields
alcohol = st.number_input('Alcohol')
malic_acid = st.number_input('Malic Acid')
ash = st.number_input('Ash')
# (add other fields similarly)

# Make prediction on button click
if st.button('Predict'):
    input_data = {
        "alcohol": alcohol,
        "malic_acid": malic_acid,
        "ash": ash,
        # Add other fields similarly
    }
    response = requests.post("http://api:8000/predict", json=input_data)
    prediction = response.json()["prediction"]
    st.write(f"The predicted wine class is: {prediction}")
