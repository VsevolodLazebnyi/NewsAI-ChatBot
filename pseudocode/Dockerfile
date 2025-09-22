FROM python:3.8-slim as builder

# Псевдокод / Pseudocode

RUN apt-get update && \
    git

RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip wheel setuptools && \
    pip install --no-cache-dir -r requirements.txt

COPY --from=builder /opt/venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"

RUN apt-get update 

COPY . /code
WORKDIR /code

CMD ["python", "bot/bot.py"]