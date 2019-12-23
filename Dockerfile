FROM python:3.6
FROM pandas
FROM botocore

ADD Hello.py /

RUN pip install pystrich

CMD [ "python", "./Hello.py" ]