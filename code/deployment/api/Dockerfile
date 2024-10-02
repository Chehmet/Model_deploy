# Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

WORKDIR /app

COPY ./code/deployment/api/main.py /app/
# COPY /models/random_forest_model.pkl /app/
COPY ../../../models/air_quality_model.pkl /app/
RUN pip install joblib pandas scikit-learn

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]



