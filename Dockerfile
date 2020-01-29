FROM python:3

ADD API.py /

RUN pip install -r requirements.txt

CMD [ "python", "./my_script.py" ]