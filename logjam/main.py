import click
import coloredlogs
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

color_logger = logging.getLogger('colorlogger')
coloredlogs.install(logger=color_logger)

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
        color_logger.log(level, log["msg"])
        print('Testing')
        time.sleep(random.randint(1,10))

def stacktrace():
    datafile = os.path.join(os.path.split(__file__)[0], 'java_stacktrace.txt')
    with open(datafile,'r') as fh:
      clj_stacktrace = fh.readlines()
    for line in clj_stacktrace:
        sys.stdout.write(line)