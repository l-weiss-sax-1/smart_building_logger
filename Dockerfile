FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-root

CMD ["python", "main.py"]
