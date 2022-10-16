ARG GIT_ACCESS_TOKEN

# GitHub
RUN git config --global url."https://$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@github.com".insteadOf "ssh://git@github.com"

FROM python:3.6-slim
WORKDIR /app
COPY requirements.txt .
COPY trained_model.pkl
RUN pip install -r requirements.txt
ENTRYPOINT [“python”, “app.py”]
