FROM python:3.14.6-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8084

ENV DATABASE_URL="mysql+pymysql://user:pass@host:port/db"

CMD [ "python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8084"]


