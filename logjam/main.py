import click
import datetime
import logging
import lorem
import random
import time
import os.path
import sys
from pythonjsonlogger import jsonlogger


logger = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
logger.addHandler(logHandler)

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
        logging.log(level, log)
        if random.choice((True, False, False, False, False)):
            stacktrace()
        time.sleep(random.randint(1,10))

def stacktrace():
    datafile = os.path.join(os.path.split(__file__)[0], 'java_stacktrace.txt')
    with open(datafile,'r') as fh:
      clj_stacktrace = fh.readlines()
    for line in clj_stacktrace:
        sys.stdout.write(line)