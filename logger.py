from sys import stdout
from enum import IntEnum
from datetime import datetime

history = []

prefix = ['DEBUG', 'INFO ', 'WARN ', 'ERROR', 'FATAL']
color = ['\x1b[0;37m','\x1b[1;36m','\x1b[0;33m','\x1b[1;31m','\x1b[0;31m']
clear = '\x1b[0m'

class LogLevel(IntEnum):
    DEBUG = 0
    INFO = 1
    WARN = 2
    ERROR = 3
    FATAL = 4

class Logger():
    def __init__(self, log_level):
        self.level = log_level

    def clear(self):
        print('\x1b[2J\x1b[;H')

    def debug(self, message):
        self.log(message)
    
    def info(self, message):
        self.log(message, LogLevel.INFO)
    
    def warn(self, message):
        self.log(message, LogLevel.WARN)

    def error(self, message):
        self.log(message, LogLevel.ERROR)

    def fatal(self, message):
        self.log(message, LogLevel.FATAL)

    def log(self, message, level=LogLevel.DEBUG):
        if(self.level <= level):
            text = f"{color[level]}<{datetime.now().strftime('%H:%M:%S')}> [{prefix[level]}]: {message}{clear}"
            print(text)
            history.append(text)
