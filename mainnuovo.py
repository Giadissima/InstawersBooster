from src.logger import Logger
from src.costants import ERROR_LOG_PATH, LOG_PATH

from logging import ERROR, DEBUG


# from logger.py
error_log = Logger.setup_logger("error", ERROR_LOG_PATH, ERROR)
log = Logger.setup_logger(file_path=LOG_PATH, level=DEBUG)

def main():
    pass
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.info("uscita...")