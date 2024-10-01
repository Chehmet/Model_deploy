from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

model = joblib.load('../../../models/air_quality_model.pkl')

class AirQualityInput(BaseModel):
    co2: float
    pm25: float
    pm10: float
    o3: float
    no2: float
    so2: float

app = FastAPI()

@app.post("/predict")
def predict_air_quality(input_data: AirQualityInput):
    data = np.array([[input_data.co2, input_data.pm25, input_data.pm10, input_data.o3, input_data.no2, input_data.so2]])
    prediction = model.predict(data)[0]
    return {"prediction": int(prediction)}
