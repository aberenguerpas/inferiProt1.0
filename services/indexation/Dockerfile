FROM python:3.10
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install torch
RUN pip install -r requirements.txt
RUN apt-get -y install curl
RUN chmod 1777 /tmp
RUN apt-get clean
RUN apt-get -y update
RUN apt-get install -y cron
RUN pip install opendatacrawler
COPY . .
ADD crontab /etc/cron.d/my-cron-file
RUN chmod 0644 /etc/cron.d/my-cron-file
RUN crontab /etc/cron.d/my-cron-file
ENTRYPOINT ["cron", "-f"]
