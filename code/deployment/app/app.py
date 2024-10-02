import streamlit as st
import requests

st.title('Air Quality Classifier')

default_co2 = 2.2
default_pm25 = 940  
default_pm10 = 131  
default_o3 = 1584   
default_no2 = 113   
default_so2 = 1056 

co2 = st.number_input('CO2', value=default_co2)
pm25 = st.number_input('PT08.S5(O3)', value=default_pm25)
pm10 = st.number_input('PT08.S4(NO2)', value=default_pm10)
o3 = st.number_input('O3 (ppm)', value=default_o3)
no2 = st.number_input('NO2 (ppm)', value=default_no2)
so2 = st.number_input('NOx (GT)', value=default_so2)

if st.button('Predict'):
    input_data = {
        "co2": co2,
        "pm25": pm25,
        "pm10": pm10,
        "o3": o3,
        "no2": no2,
        "so2": so2,
    }
    response = requests.post("http://api:8000/predict", json=input_data)

    # response = requests.post("http://localhost:8000/predict", json=input_data)  # Make sure FastAPI is running locally
    prediction = response.json()["prediction"]

    if prediction == 1:
        st.write("The air quality is appropriate for humans.")
    else:
        st.write("The air quality is not appropriate for humans.")
