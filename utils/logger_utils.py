"""
File to put all logger util methods
"""
import logging


def bootstrap_logger(name, logfile='error.log') -> logging.Logger:
    """
    Return a logger obj
    """
    formatter = logging.Formatter(
        "%(asctime)s %(filename)s (%(funcName)s, %(lineno)d) [%(levelname)s] - %(message)s")
    handler = logging.FileHandler(f'logs/{logfile}')
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    return logger
