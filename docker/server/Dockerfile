FROM nginx:1.15.6-alpine

LABEL maintainer="Michał Wiśniewski <mikex929@gmail.com>"
LABEL description="Fitness Clubb - main server application"

RUN rm /etc/nginx/conf.d/default.conf
RUN mkdir -p /fitness_club/static && \
    mkdir -p /fitness_club/media

WORKDIR /fitness_club
COPY ./conf/fitness_club_nginx.conf /etc/nginx/conf.d/

EXPOSE 80
EXPOSE 8000

CMD ["nginx", "-g", "daemon off;"]