import click
import datetime
import logging
import lorem
import random
import time
import os.path
import sys
from pythonjsonlogger import jsonlogger


json_logger = logging.getLogger('jsonlogger')
json_logHandler = logging.StreamHandler()
json_formatter = jsonlogger.JsonFormatter()
json_logHandler.setFormatter(json_formatter)
json_logger.addHandler(json_logHandler)


@click.command()
def cli():
    word_count = len(lorem.data.WORDS) - 1
    while True:
        level = random.randint(0,5) * 10
        log = {
            'msg': lorem.sentence(),
            'level': logging.getLevelName(level),
            'timestamp': datetime.datetime.now(datetime.timezone.utc),
            'ns': f'{lorem.data.WORDS[random.randint(0,word_count)]}.{lorem.data.WORDS[random.randint(0,word_count)]}'
        }
        json_logger.log(level, log)
        print(f'\033[3{int(level/10)+1}m{log["level"]}\033[0m: {level/10} {log["msg"]}')
        time.sleep(random.randint(1,10))

def stacktrace():
    datafile = os.path.join(os.path.split(__file__)[0], 'java_stacktrace.txt')
    with open(datafile,'r') as fh:
      clj_stacktrace = fh.readlines()
    for line in clj_stacktrace:
        sys.stdout.write(line)