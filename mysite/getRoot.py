import os
import time

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
current_date = time.strftime("%Y-%m-&d", time.localtime(time.time()))


def get_root():
    return ROOT_DIR


def get_current_date():
    return current_date
