import sys
from decouple import config
from aws import S3
from utils.commands import delete_file, dump_and_compress, limit_date_lte, set_log


def main():
    try:
        day = int(sys.argv[1])
    except Exception as e:
        set_log("Parameter: " + str(e))
        set_log("Parameter day default 7")
        day = 7

    bucket = S3(bucket=config("BUCKET"))
    list_objects = bucket.list_objects()
    objects_to_delete = [
        {"Key": obj.key}
        for obj in list_objects
        if limit_date_lte(day, obj.last_modified)
    ]

    if objects_to_delete:
        bucket.delete_objects(objects_to_delete)

    try:
        tar_name, is_ok = dump_and_compress()
        if is_ok:
            bucket.upload_object(tar_name)
            delete_file(file_name=tar_name)
    except Exception as e:
        set_log(str(e))

    # criar um sistema de log

if __name__ == "__main__":
    main()
