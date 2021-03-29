from botocore.exceptions import ClientError
import logging
import boto3
import os 
import zipfile

my_path = '/home/mo/Desktop/test'
my_file = "test.zip"
BUCKET_NAME = 'mohamedsalembuket' # replace with your bucket name

#upload S3 files
uploadeds3 = boto3.client('s3')
os.chdir(my_path)
with open( my_file , 'rb') as f:
  uploadeds3.upload_fileobj(f,BUCKET_NAME, my_file)