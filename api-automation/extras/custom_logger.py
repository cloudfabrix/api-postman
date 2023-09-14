# Example usage:
# custom_logger = CustomLogger()
# logger = custom_logger.get_logger()
# logger.debug("Debug message")
# logger.info("Info message")
# logger.warning("Warning message")
# logger.error("Error message")
# logger.critical("Critical message")

import logging
from logging.handlers import RotatingFileHandler

class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger('api_automation')
        if not self.logger.handlers:
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
        my_format = '%(asctime)s %(levelname)s %(module)s: %(message)s'

        FORMATS = {
            logging.DEBUG: my_format,
            logging.INFO: my_format,
            logging.WARNING: my_format,
            logging.ERROR: my_format,
            logging.CRITICAL: my_format
        }

        def __init__(self):
            super().__init__(self.my_format)

        def format(self, record):
            log_fmt = self.FORMATS.get(record.levelno)
            self._style = logging.PercentStyle(log_fmt)
            return super().format(record)
