###########################################
# Dockerfile to build an Django image
###########################################
# Base image is python:3.5
FROM python:3.5

# Author Mr.Trinh
MAINTAINER Mr.Trinh <loi.trinhxuan@asnet.com.vn>

ENV PYTHONUNBUFFERED 1

COPY ./requirements /requirements

RUN pip install -r /requirements/local.txt

COPY ./shell-scripts/entrypoint.sh /entrypoint.sh

RUN sed -i 's/\r//' /entrypoint.sh && chmod +x /entrypoint.sh

COPY ./shell-scripts/start.sh /start.sh

RUN sed -i 's/\r//' /start.sh && chmod +x /start.sh

WORKDIR /app

ENTRYPOINT ["/entrypoint.sh"]
