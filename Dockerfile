FROM python:3.6
FROM ibm-cos-sdk
ADD Hello.py /

RUN pip install pystrich
RUN pip install pandas
RUN pip install botocore
RUN pip install ibm_boto3

CMD [ "python", "./Hello.py" ]