import boto3
from decouple import config
from typing import List, Optional
from botocore.exceptions import ClientError
from utils import datetime_now, set_log


class S3Bucket:
    def __init__(self, bucket, bucket_folder=config("BUCKET_FOLDER")):
        self.client = boto3.client('s3')
        self.session = boto3.Session()
        self.bucket = bucket
        self.bucket_folder = bucket_folder

    def upload_object(self, file_name: str, local_folder="./") -> bool:
        local_basename = local_folder + file_name
        bucket_basename = self.bucket_folder + file_name    
        
        with open(local_basename, "rb") as f:
            try:
                self.client.upload_fileobj(f, self.bucket, bucket_basename)
            except ClientError as e:
                set_log(e)
                return False
        return True

    def list_objects(self) -> Optional[List]:
        try:
            s3 = self.session.resource('s3')
            my_bucket = s3.Bucket(self.bucket)
            return my_bucket.objects.filter(Prefix=self.bucket_folder)
                # last_modified
        except ClientError as e:
            set_log(e)
            return None
