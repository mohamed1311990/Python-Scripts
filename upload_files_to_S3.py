from botocore.exceptions import ClientError
import logging
import boto3
import os 
import zipfile

my_path = '/home/mo/Desktop/test/work'
my_file = "/home/mo/Desktop/test/test.zip"
BUCKET_NAME = 'mohamedsalembuket' # replace with your bucket name

#upload S3 files
uploadeds3 = boto3.client('s3')
for local_file in os.listdir(my_path):
   os.chdir(my_path)
   with open(local_file, 'rb') as f:
      uploadeds3.upload_fileobj(f,BUCKET_NAME,local_file)