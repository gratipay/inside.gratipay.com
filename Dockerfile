#Base image
FROM python:2.7.14-alpine

#Install make and some other dependencies
RUN apk --no-cache add \
    make \
    g++

#Move the source code to /inside.gratipay.com inside the container
COPY . /inside.gratipay.com
WORKDIR /inside.gratipay.com

#Set up the environment
RUN make env

CMD ["make", "run"]