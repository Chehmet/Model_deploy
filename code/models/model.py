
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib


data = pd.read_csv(r'code\datasets\AirQuality.csv', delimiter=';')
data = data.drop(columns=['Date', 'Time'])

data = data.apply(lambda x: x.str.replace(',', '.').astype(float) if x.dtype == 'object' else x)
data = data[['CO(GT)', 'PT08.S5(O3)', 'NO2(GT)', 'PT08.S4(NO2)', 'C6H6(GT)']]
data = data.fillna(data.mean())

X = data.drop(columns=['C6H6(GT)']) 
y = (data['C6H6(GT)'] < 5).astype(int) 

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, 'models/air_quality_model.pkl')
