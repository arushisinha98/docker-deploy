FROM python:3.7
RUN git config --global url."https://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:@github.com/".insteadOf "https://github.com/"
RUN pip install Flask=0.11.1
RUN useradd -ms /bin/bash admin
USER admin
WORKDIR /app
COPY requirements.txt /app
COPY trained_model.pkl /app
RUN pip install -r requirements.txt
CMD [“python”, “app.py”]
