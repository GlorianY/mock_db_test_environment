FROM python:3.8.8

WORKDIR /usr/src/app

# remove volume
RUN rm -rf ./postgres-data/

COPY requirements.txt /usr/src/app/

RUN pip install pip --upgrade &&  pip install -r requirements.txt

COPY . /usr/src/app/
