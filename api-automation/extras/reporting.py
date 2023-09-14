# Usage: api_automation.log file
# custom_logger = CustomLogger()
# logger = custom_logger.get_logger()
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")

import logging
import os
import shutil
import re
import pathlib
from logging.handlers import RotatingFileHandler


class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger('api_automation')
        self.logger.setLevel(logging.DEBUG)

        # Create a rotating log handler with a max size of 1 MB and keep 5 backups.
        handler = RotatingFileHandler('api_automation.log', maxBytes=1e6, backupCount=5)
        formatter = self.CustomFormatter()

        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

        # Log an "END" line to separate different runs.
        self.logger.info("END")

    def get_logger(self):
        return self.logger

    class CustomFormatter(logging.Formatter):
        grey = "\x1b[38;20m"
        yellow = "\x1b[33;20m"
        red = "\x1b[31;20m"
        bold_red = "\x1b[31;1m"
        reset = "\x1b[0m"
        my_format = '%(asctime)s %(levelname)s %(module)s: %(message)s'

        FORMATS = {
            logging.DEBUG: grey + my_format + reset,
            logging.INFO: grey + my_format + reset,
            logging.WARNING: yellow + my_format + reset,
            logging.ERROR: red + my_format + reset,
            logging.CRITICAL: bold_red + my_format + reset
        }

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            formatter = logging.Formatter(log_fmt)
            return formatter.format(record)
