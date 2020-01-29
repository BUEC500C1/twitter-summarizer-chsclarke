FROM python:3

ADD API.py / 
ADD endpoint.py /

RUN pip install -r requirements.txt

RUN export FLASK_APP=endpoint.py

CMD flask run