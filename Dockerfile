FROM python

RUN apt-get -y update && apt-get -y install git \
    && git clone https://github.com/underson666666/ping-monitor-line-notify.git \
    && rm -rf /var/lib/apt/lists/*
WORKDIR ping-monitor-line-notify
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "main.py"]
