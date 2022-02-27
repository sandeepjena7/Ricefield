FROM python:3.7-buster
COPY . /app
EXPOSE 5000
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "127.0.0.1", "--port", "5000"]