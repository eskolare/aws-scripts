import os
import pytz
from decouple import config
from datetime import datetime

def command(command: str):
    os.system(command)

def set_log(msg: str):
    os.system(f"echo {msg} >> ./info.log")

def datetime_now():
    return datetime.now(pytz.UTC)

def dump():
    file_name = f"{datetime_now().strftime('%Y-%m-%d')}-bkp"
    dump_name = f"{file_name}.sql"
    command(f"PGPASSWORD={config('PGPASSWORD')} pg_dump {config('DBNAME')} -U {config('PGUSERNAME')} -h {config('HOSTNAME')} -F c > ./{dump_name}")
    return dump_name

def compress(file_name):
    tar_name = f"{file_name}.tar.gz"
    command(f"zip {tar_name} ./{file_name}")
    return tar_name

def dump_and_compress():
    dump_name = dump()
    tar_name = compress(dump_name)
    return tar_name, dump_name