# Author: Cuong Tran
#
# Build: docker build -t cuongtransc/app:0.1 .
# Run: docker run -d -p 8080:8080 --name app-run cuongtransc/app:0.1
#

FROM python:3.6-alpine
LABEL maintainer="cuongtransc@gmail.com"

ENV REFRESHED_AT 2019-01-11

COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt


COPY . /app

WORKDIR /app
# VOLUME /app

EXPOSE 5000

# # docker entrypoint
# COPY docker-entrypoint.sh /
# ENTRYPOINT ["/docker-entrypoint.sh"]

STOPSIGNAL SIGINT

CMD ["flask", "run", "--host", "0.0.0.0"]

