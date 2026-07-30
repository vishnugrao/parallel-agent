from python:slim

WORKDIR /app

COPY src/ ./src/
COPY tests/ ./tests/
COPY requirements.txt ./

RUN pip install -r requirements.txt

CMD ["pytest", "tests/", "-v"]
