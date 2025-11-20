FROM python:3.11-slim

WORKDIR /myapp

RUN apt-get update && apt-get install -y curl build-essential

RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry

ENV PATH="/root/.local/bin:$PATH"

COPY pyproject.toml poetry.lock* /myapp/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-root --no-ansi

COPY rf_model.bin /myapp/
COPY ./ /myapp/

EXPOSE 8000

CMD ["uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "8000"]

