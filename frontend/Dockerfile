FROM python:3.9.10-slim as builder

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install --upgrade pip && \
    pip install "poetry==1.2.0" && \
    poetry config virtualenvs.create false && \
    poetry install
    
COPY . .

COPY ./entrypoint.sh /app/entrypoint.sh

# copy project
COPY . /app

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

CMD ["gunicorn", "frontend.wsgi:application", "--bind", "0.0.0.0:7000"] 