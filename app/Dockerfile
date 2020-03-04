FROM python:3.6.5 as backend

WORKDIR /app

COPY . /app/
COPY requirements.txt /
COPY entrypoint.sh /

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

ENTRYPOINT ["/entrypoint.sh"]
