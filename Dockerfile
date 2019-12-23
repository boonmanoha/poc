FROM python:3.6

ADD Hello.py /

RUN pip install pystrich
RUN pip install pandas
RUN pip install botocore

CMD [ "python", "./Hello.py" ]