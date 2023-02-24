import sys
from decouple import config
from s3 import S3Bucket
from utils import dump_and_compress


def main():
    try:
        day = sys.argv[1]
    except IndexError:
        day = 7
    
    bucket = S3Bucket(bucket=config("BUCKET"))
    # tar_name, sql_name = dump_and_compress()
    # bucket.upload_object(tar_name)
    objects = bucket.list_objects()
    
    
    # Se sucesso apagar o arquivo sql e o tar gz local
    # If success, verify if you can remove tar.gz older


    # criar um sistema de log, e tentar novamente caso não de certo

if __name__ == "__main__":
    main()