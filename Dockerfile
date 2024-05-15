FROM python:3.10-slim-buster

WORKDIR /test_api

USER root

# Copy Python script
COPY ./test_api .

RUN apt-get update && apt-get install -y --no-install-recommends libmagic1

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /test_api

# install dependencies
RUN pip install -r requirements.txt

# Run script with xvfb
CMD ["pytest", "-v", "--html=report.html", "--self-contained-html"]
