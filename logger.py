import logging

class Logger:
    def __init__(self, file_name):
        logging.basicConfig(filename=file_name,level=logging.DEBUG)
        self.info = logging.info
        self.debug = logging.debug
        self.error = logging.error
        self.critical = logging.critical

    def start(self):
        self.info("Start program")

    def quit(self):
        self.info("Endo program\n")
