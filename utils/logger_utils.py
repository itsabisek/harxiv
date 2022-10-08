"""
File to put all logger util methods
"""
import logging


def bootstrap_logger(name, logfile='error.log') -> logging.Logger:
    """
    Return a logger obj
    """
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        "%(asctime)s %(filename)s (%(funcName)s, %(lineno)d) [%(levelname)s] - %(message)s")
    handler = logging.FileHandler(f'logs/{logfile}')
    handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.addHandler(handler)
    return logger
