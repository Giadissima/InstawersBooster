import logging
from datetime import datetime

class Logger:
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
    def setup_logger(name="default", file_path="default.log", level=logging.INFO):
        """To setup many loggers"""
        if not logging.getLogger(name).hasHandlers():
            logger = logging.getLogger(name)
            logger.setLevel(level)

            fileHandler = logging.FileHandler(file_path, encoding="utf-8")
            fileHandler.setLevel(level)
            fileHandler.setFormatter(Logger.formatter)

            logger.addHandler(fileHandler)
            return logger
        else:
            return logging.getLogger(name)