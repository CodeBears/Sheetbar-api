import logging
import os
import sys
from logging.handlers import TimedRotatingFileHandler


class LogTool:
    @staticmethod
    def _init_file_path():
        os.makedirs('static/logs', exist_ok=True)

    @staticmethod
    def set_print_in_terminal(logger):
        logger.addHandler(logging.StreamHandler(sys.stdout))

    @staticmethod
    def set_log_file_by_day(logger, filename):
        time_handler = TimedRotatingFileHandler(
            filename=filename,
            when="midnight",
            interval=1
        )
        time_handler.suffix = "%Y%m%d"
        logger.addHandler(time_handler)

    @classmethod
    def init_logging(cls):
        cls._init_file_path()
        logging.basicConfig(level=logging.WARNING)
        logger = logging.getLogger()
        cls.set_print_in_terminal(logger=logger)
        cls.set_log_file_by_day(logger=logger, filename='static/logs/logs.log')
        return logging
