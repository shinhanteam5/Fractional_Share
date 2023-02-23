FROM python:3.11.2

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt
RUN cd fractional_share && python manage.py migrate

USER root
EXPOSE 8000

CMD ["/bin/bash", "gunicorn_start"]