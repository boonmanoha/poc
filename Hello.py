print("Hello Ravi")
print("Hello Boon")
print("Hello abhi")

import types
import pandas as pd
from botocore.client import Config
import ibm_boto3

def __iter__(self): return 0
# @hidden_cell
# The following code accesses a file in your IBM Cloud Object Storage. It includes your credentials.
# You might want to remove those credentials before you share the notebook.
client_13c23d660be64684ae8b80a9d8923863 = ibm_boto3.client(service_name='s3',
    ibm_api_key_id='KFAu8ytT0mikJ9aOLOapLHLPMPl8AVBQ5vJkXJmW5LB8',
    ibm_auth_endpoint="https://iam.eu-gb.bluemix.net/oidc/token",
    config=Config(signature_version='oauth'),
    endpoint_url='https://s3.eu-geo.objectstorage.service.networklayer.com')
# Your data file was loaded into a botocore.response.StreamingBody object.
# Please read the documentation of ibm_boto3 and pandas to learn more about the possibilities to load the data.
# ibm_boto3 documentation: https://ibm.github.io/ibm-cos-sdk-python/
# pandas documentation: http://pandas.pydata.org/
streaming_body_1 = client_13c23d660be64684ae8b80a9d8923863.get_object(Bucket='pnwstestbipractise-donotdelete-pr-ufyrjd7t8exufv', Key='bi.txt')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(streaming_body_1, "__iter__"): streaming_body_1.__iter__ = types.MethodType( __iter__, streaming_body_1 )
body = client_13c23d660be64684ae8b80a9d8923863.get_object(Bucket='pnwstestbipractise-donotdelete-pr-ufyrjd7t8exufv',Key='Desc.csv')['Body']
# add missing __iter__ method, so pandas accepts body as file-like object
if not hasattr(body, "__iter__"): body.__iter__ = types.MethodType( __iter__, body )
# If you are reading an Excel file into a pandas DataFrame, replace `read_csv` by `read_excel` in the next statement.
df_data_0 = pd.read_csv(body)
df_data_0.head()
print(df_data_0)