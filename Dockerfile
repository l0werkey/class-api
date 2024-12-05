FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN python -m venv .venv

RUN .venv/bin/pip install --upgrade pip && \
    .venv/bin/pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_ENV=production

CMD [".venv/bin/python", "-m", "flask", "run"]
