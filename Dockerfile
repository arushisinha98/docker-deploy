FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt .
COPY trained_model.pkl
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT [“python”, “app.py”]
