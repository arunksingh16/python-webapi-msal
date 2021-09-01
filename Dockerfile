FROM python:3.8
ENV SERVER_IP="0.0.0.0"
ENV SERVER_PORT="5000"
COPY .  /app/
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
