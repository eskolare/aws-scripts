from decouple import config
from aws import S3
from utils.commands import delete_file, dump_and_compress, limit_date_lte
from utils.args import get_limit_day, is_production
from log.logging import error_log
from log.sentry import start_sentry


def main():
    day = get_limit_day()
    if is_production():
        start_sentry()

    bucket = S3(bucket=config("BUCKET"))
    objects = bucket.list_objects()
    if objects:
        objects_to_delete = [
            {"Key": obj.key}
            for obj in objects
            if limit_date_lte(day, obj.last_modified)
        ]

        if objects_to_delete:
            bucket.delete_objects(objects_to_delete)

    try:
        tar_name, is_ok = dump_and_compress()
        if is_ok:
            bucket.upload_object(tar_name)
            delete_file(file_name=tar_name)
        else:
            error_log("dump_and_compress method dind't work.")
    except Exception as e:
        error_log(str(e))


if __name__ == "__main__":
    main()
