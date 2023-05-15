import click
import colorlog
import datetime
import logging
import lorem
import random
import time
import os.path
import sys
from pythonjsonlogger import jsonlogger


json_logger = logging.getLogger('jsonlogger')
json_logger.setLevel(logging.DEBUG)
json_handler = logging.StreamHandler()
json_logger.addHandler(json_handler)
json_handler.setFormatter(jsonlogger.JsonFormatter())

color_logger = colorlog.getLogger('colorlogger')
color_logger.setLevel(logging.DEBUG)
color_handler = colorlog.StreamHandler()
color_logger.addHandler(color_handler)
color_handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s %(asctime)s %(blue)s%(message)s"
        )
)

text_logger = logging.getLogger('textlogger')
text_logger.setLevel(logging.DEBUG)
text_handler = logging.StreamHandler()
text_logger.addHandler(text_handler)
text_handler.setFormatter(
    logging.Formatter('%(levelname)-8s %(asctime)s %(message)s')
)

@click.command()
@click.option('--min-delay', default=1, help='Minimum number of seconds between log messages.')
@click.option('--max-delay', default=10, help='Maximum number of seconds between log messages.')
@click.option('--delay', default=None, type=click.FLOAT, help='Number of seconds between log messages.')
@click.option('--format',
              type=click.Choice(['json', 'text', 'color-text'], case_sensitive=False),
              default='json')
def cli( min_delay, max_delay, delay, format):
    word_count = len(lorem.data.WORDS) - 1
    while True:
        level = random.randint(0,5) * 10
        log = {
            'message': lorem.sentence(),
            'level': logging.getLevelName(level),
            'timestamp': datetime.datetime.now(datetime.timezone.utc),
        }

        if format == 'json':
            json_logger.log(level, log)
        elif format == 'color-text':
            color_logger.log(level, log["message"])
        elif format == 'text':
            text_logger.log(level, log["message"])

        if delay == None:
            time.sleep(random.randint(min_delay, max_delay))
        else:
            time.sleep(delay)
