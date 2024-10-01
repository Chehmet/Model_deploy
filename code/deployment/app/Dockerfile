# Dockerfile
FROM python:3.9

WORKDIR /app

COPY ./app.py /app/

RUN pip install streamlit requests pandas

CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
