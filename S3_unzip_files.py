
#aaa
import logging
import boto3
import os 
import zipfile

def myfunction(event,context):
  BUCKET_NAME = 'mohamedsalembuket'  # replace with your bucket name
  KEY = 'test.zip'                   # replace with your object key
  downloaded_zip = '/tmp/downloaded.zip'   #downloaded zip file path
  extracted_files_path = '/tmp/work'       #extracted files location

  # download S3 bucket
  mys3 = boto3.resource('s3')
  # os.chdir('/tmp')
  mys3.Bucket('mohamedsalembuket').download_file(KEY,downloaded_zip)

  #extract S3 bucket files
  with zipfile.ZipFile(downloaded_zip, 'r') as zip_ref:
      zip_ref.extractall(extracted_files_path)

  #upload extracted S3 files
  uploadeds3 = boto3.client('s3')
  for local_file in os.listdir(extracted_files_path):
    os.chdir(extracted_files_path)
    with open(local_file, 'rb') as f:
      uploadeds3.upload_fileobj(f,BUCKET_NAME,local_file) 

