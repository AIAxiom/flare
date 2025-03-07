import logging
import os
from logging.handlers import RotatingFileHandler


def setup_logger(name: str, level: int = logging.DEBUG, log_file: str = None):
    """
    Logger with a console handler and an optional file handler.

    :param name: Name of the logger
    :param log_file: Optional file to store logs
    :param level: Logging level
    :return: Configured logger instance
    """
    fmt = "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
    if level == logging.DEBUG:
        fmt = "%(asctime)s | %(levelname)s | %(name)s | %(filename)s:%(lineno)d | %(message)s"

    formatter = logging.Formatter(
        fmt,
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    logger = logging.getLogger(name)
    logger.setLevel(level)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(level)
    logger.addHandler(console_handler)

    # Optional file handler
    if log_file:
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        file_handler = RotatingFileHandler(log_file, maxBytes=5 * 1024 * 1024, backupCount=5)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(level)
        logger.addHandler(file_handler)

    logger.propagate = False
    return logger


# Example usage
if __name__ == "__main__":
    log = setup_logger("my_logger")
    log.debug("This is a debug message")
    log.info("This is an info message")
    log.warning("This is a warning message")
    log.error("This is an error message")
    log.critical("This is a critical message")
