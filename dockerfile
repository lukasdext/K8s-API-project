FROM python:3.9

WORKDIR /app

COPY app.py /app

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]

#http://localhost:5000/api/data
