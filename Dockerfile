FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install flask pytest

CMD ["python", "app.py"]