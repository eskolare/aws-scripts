from logging import basicConfig, error, ERROR

basicConfig(
    level=ERROR,
    filename="info.log",
    filemode="a",
    encoding="utf-8",
    format="%(levelname)s:%(asctime)s:%(message)s",
    datefmt="%Y-%m-%d",
)


def error_log(msg: str):
    list_message = msg.split("\n")
    if len(list_message) > 1:
        error(list_message[0])
    else:
        error(msg)
