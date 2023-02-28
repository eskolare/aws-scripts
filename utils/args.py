import sys
from utils.constants import Environments


def get_limit_day() -> int:
    try:
        return int(sys.argv[1])
    except Exception as e:
        return 7


def is_production() -> bool:
    try:
        return sys.argv[2] == Environments.PRODUCTION
    except Exception:
        return False
