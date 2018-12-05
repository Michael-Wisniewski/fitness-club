FROM alpine:3.8

LABEL maintainer="Michał Wiśniewski <mikex929@gmail.com>"
LABEL description="Fitness Clubb - main application"

RUN mkdir -p /fitness_club/src && \
    mkdir /fitness_club/static && \
    mkdir /fitness_club/media
WORKDIR /fitness_club
COPY ./conf ./

RUN apk update && \
    apk upgrade
RUN apk add --update --no-cache \
        python3 \
        python3-dev \
        build-base \
        linux-headers \
        pcre-dev \
        postgresql-dev \
        musl-dev \
        nodejs \
        nodejs-npm

RUN pip3 install --no-cache-dir -r requirements.txt

RUN addgroup -g 1000 -S uwsgi_group && \
    adduser -D -H -u 1000 -S uwsgi_admin -G uwsgi_group

USER uwsgi_admin

EXPOSE 8000

CMD ["uwsgi", "--ini", "uwsgi.ini"]