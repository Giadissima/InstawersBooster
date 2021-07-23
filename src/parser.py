import argparse
from src.logger import Logger
from logging import ERROR

class Parser:
    def __init__(self, description=""):
        self.parser = argparse.ArgumentParser(description=description)

    def arguments(self):
        self.parser.add_argument(
            "-l", "--logpath", required=False, type=str, help="Set where you want to save info and error logs")
        self.parser.add_argument(
            "-u", "--username", required=False, type=str, help="Insert user's username")
        self.parser.add_argument(
            "-p", "--password", required=False, type=str, help="Insert user's password")
        self.parser.add_argument(
            "-c", "--chromedriverpath", required=False, type=str, help="Path where chromedriver.exe is saved")


        return vars(self.parser.parse_args())

        