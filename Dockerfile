FROM python:3.8-slim-buster

EXPOSE 8080

RUN pip3 install --upgrade pip

# Install pip requirements
ADD requirements.txt /opt/app/requirements.txt

WORKDIR /opt/app

RUN pip3 install -r requirements.txt

COPY . /opt/app

CMD ["gunicorn", "-b", "0.0.0.0:8080", "wsgi:application"]