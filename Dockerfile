FROM python:3.10

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app

CMD ["fastapi", "run", "src/main.py"]
