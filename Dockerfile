FROM python:3.6.4

ARG IMAGE_PORT
ARG IMAGE_HOST
ENV IMAGE_PORT=${IMAGE_PORT}
ENV IMAGE_HOST=${IMAGE_HOST}

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE ${IMAGE_PORT}

ENTRYPOINT ["python3"]

CMD ["-m", "server"]
