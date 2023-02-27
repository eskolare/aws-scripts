import boto3
from decouple import config
from typing import List, Optional
from botocore.exceptions import ClientError
from utils.commands import set_log


class S3:
    def __init__(self, bucket, bucket_folder=config("BUCKET_FOLDER")):
        self.client = boto3.client("s3")
        self.session = boto3.Session()
        self.bucket = bucket
        self.bucket_folder = bucket_folder

    def upload_object(self, file_name: str, local_folder="./") -> bool:
        local_basename = local_folder + file_name
        bucket_basename = self.bucket_folder + file_name

        with open(local_basename, "rb") as f:
            try:
                self.client.upload_fileobj(f, self.bucket, bucket_basename)
            except Exception as e:
                set_log(str(e))
                return False
        return True

    def list_objects(self) -> Optional[List]:
        try:
            s3 = self.session.resource("s3")
            my_bucket = s3.Bucket(self.bucket)
            return list(my_bucket.objects.filter(Prefix=self.bucket_folder))[1:]
        except Exception as e:
            set_log(str(e))
            return None

    def delete_objects(self, objects: List) -> bool:
        delete_data = {"Objects": objects, "Quiet": True}
        try:
            self.client.delete_objects(Bucket=self.bucket, Delete=delete_data)
            return True
        except Exception as e:
            set_log(str(e))
            return False
