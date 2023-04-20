ARG PYTHON_VERSION=3.10.8-slim-buster

FROM python:${PYTHON_VERSION}

ARG APP_ROOT=/app

WORKDIR ${APP_ROOT}

COPY . ${APP_ROOT}
COPY ./docker/start.sh /usr/bin/docker-start.sh
COPY ./docker/entrypoint.sh /usr/bin/docker-entrypoint.sh

RUN pip install -r requirements/local.txt
RUN chmod +x \
    /usr/bin/docker-start.sh \
    /usr/bin/docker-entrypoint.sh

ENTRYPOINT [ "/usr/bin/docker-entrypoint.sh" ]
