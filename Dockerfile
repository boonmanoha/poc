FROM python:3.6

ADD Hello.py /

RUN pip install pystrich

CMD [ "python", "./Hello.py" ]