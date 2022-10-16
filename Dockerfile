ARG GIT_ACCESS_TOKEN

# GitHub
RUN git config --global url."https://${GIT_ACCESS_TOKEN}@github.com".insteadOf "ssh://git@github.com"

FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt .
COPY trained_model.pkl
RUN pip install -r requirements.txt
ENTRYPOINT [“python”, “app.py”]
