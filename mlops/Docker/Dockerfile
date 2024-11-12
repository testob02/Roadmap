FROM python:3.12.2-alpine

COPY package.txt /app/
COPY src /app/

WORKDIR /app

RUN pip install -r package.txt

CMD ["uvicorn", "server:app", "--host", "0.0.0.0", "--port", "8000"]