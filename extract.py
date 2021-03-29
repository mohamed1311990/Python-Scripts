from botocore.exceptions import ClientError
import logging
import boto3
import os 
import zipfile

# download S3 bucket
BUCKET_NAME = 'mohamedsalembuket' # replace with your bucket name
KEY = 'test.zip' # replace with your object key
mys3 = boto3.resource('s3')
try:
    mys3.Bucket('mohamedsalembuket').download_file(KEY,'test.zip')
except botocore.exceptions.ClientError as e:
    if e.response['Error']['Code'] == "404":
        print("The object does not exist.")
    else:
        raise

#extract S3 bucket files
my_path = '/home/mo/Desktop/test/work'
my_file = "/home/mo/Desktop/test/test.zip"
with zipfile.ZipFile(my_file, 'r') as zip_ref:
    zip_ref.extractall(my_path)


#upload S3 files
uploadeds3 = boto3.client('s3')
for local_file in os.listdir(my_path):
   os.chdir(my_path)
   with open(local_file, 'rb') as f:
      uploadeds3.upload_fileobj(f,BUCKET_NAME,local_file)