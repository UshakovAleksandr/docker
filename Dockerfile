FROM python:3.8
COPY . .
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["gunicorn", "app:app"]