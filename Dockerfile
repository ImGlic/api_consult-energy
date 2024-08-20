FROM python:3.11.3-alpine3.18
LABEL mantainer="vitooj@outlook.com"

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./website /website
COPY ./entrypoint.sh /entrypoint.sh

WORKDIR /website

EXPOSE 8000

RUN python -m venv /venv && \
    /venv/bin/pip install --upgrade pip && \
    /venv/bin/pip install -r /website/requirements.txt && \
    adduser --disabled-password --no-create-home duser && \
    chown -R duser:duser /website && \
    chmod +x /entrypoint.sh


ENV PATH="/scripts:/venv/bin:$PATH"

ENTRYPOINT ["/entrypoint.sh"]
