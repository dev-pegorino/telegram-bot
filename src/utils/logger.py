import logging
import sys

from colorama import Fore, Style, init

from src.config import settings

init(autoreset=True)


class ColoredFormatter(logging.Formatter):
    COLORS = {
        'INFO': Fore.GREEN,
        'WARNING': Fore.YELLOW,
        'ERROR': Fore.RED,
        'CRITICAL': Fore.RED + Style.BRIGHT,
        'DEBUG': Fore.CYAN,
    }

    def format(self, record):
        level_color = self.COLORS.get(record.levelname, '')
        message = super().format(record)
        return f"{level_color}{message}"


console_formatter = ColoredFormatter(fmt=settings.LOG_FORMAT, datefmt=settings.LOG_DATE_FORMAT)
file_formatter = logging.Formatter(fmt=settings.LOG_FORMAT, datefmt=settings.LOG_DATE_FORMAT)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(console_formatter)

file_handler = logging.FileHandler(settings.LOG_FILE, encoding='utf-8')
file_handler.setFormatter(file_formatter)


logging.basicConfig(level=settings.LOG_LEVEL, handlers=[console_handler, file_handler])


def logger_func(name_file: __name__): return logging.getLogger(name_file)