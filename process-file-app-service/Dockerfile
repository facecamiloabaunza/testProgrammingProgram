FROM alpine:3.10

RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip3 --no-cache-dir install -r requirements.txt

COPY . /app

CMD python3 main.py
