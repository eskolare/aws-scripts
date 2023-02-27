import os
import pytz
from typing import List, Tuple
from decouple import config
from utils.constants import COMMAND_SUCCESS
from datetime import datetime, timedelta


def command(command: str) -> int:
    return os.system(command)


def is_ok(res) -> bool:
    return res == COMMAND_SUCCESS


def datetime_utcnow():
    return datetime.now(pytz.UTC)


def set_log(msg: str):
    date_str = datetime_utcnow().strftime('%Y-%m-%d')
    list_message = msg.split("\n")
    if len(list_message) == 1:
        os.system(f"echo {date_str}: {list_message[0]} >> ./info.log")
    else:
        os.system(f"echo {date_str}: {list_message[0]} >> ./info.log")
        for m in list_message[1:]:
            os.system(f"echo {m} >> ./info.log")


def delete_file(file_name: str):
    command(f"rm {file_name}")


def limit_date_lte(day, date) -> bool:
    limit = datetime_utcnow() - timedelta(days=day)
    return date <= limit


def dump() -> Tuple[str, bool]:
    file_name = f"{datetime_utcnow().strftime('%Y-%m-%d')}-bkp"
    dump_name = f"{file_name}.sql"
    res = command(
        f"PGPASSWORD={config('PGPASSWORD')} pg_dump {config('DBNAME')} -U {config('PGUSERNAME')} -h {config('HOSTNAME')} -F c > ./{dump_name}"
    )
    return dump_name, is_ok(res)


def compress(file_name) -> Tuple[str, bool]:
    tar_name = f"{file_name}.tar.gz"
    res = command(f"zip {tar_name} ./{file_name}")
    return tar_name, is_ok(res)


def dump_and_compress() -> Tuple[str, bool]:
    tar_name = ""
    dump_name, is_ok = dump()
    if is_ok:
        tar_name, is_ok = compress(dump_name)
        if is_ok:
            delete_file(dump_name)
    else:
        delete_file(dump_name)
    return tar_name, is_ok
