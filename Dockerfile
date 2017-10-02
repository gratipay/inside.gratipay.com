FROM python:2.7.14-alpine

RUN apk --no-cache add \
    make \
    g++

COPY . /inside.gratipay.com
WORKDIR /inside.gratipay.com

RUN make env

EXPOSE 8563

CMD ["make", "run"]