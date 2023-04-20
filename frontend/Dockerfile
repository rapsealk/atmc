ARG NODE_VERSION=18.16-buster-slim

FROM node:${NODE_VERSION}

ARG APP_ROOT=/app

WORKDIR ${APP_ROOT}

COPY . ${APP_ROOT}
COPY ./docker/start.sh /usr/bin/docker-start.sh
COPY ./docker/entrypoint.sh /usr/bin/docker-entrypoint.sh

RUN yarn && yarn build
RUN chmod +x \
    /usr/bin/docker-start.sh \
    /usr/bin/docker-entrypoint.sh

ENTRYPOINT [ "/usr/bin/docker-entrypoint.sh" ]
