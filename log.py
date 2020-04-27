import logging


def NewLogger(name=None):
    log_file = 'anchor.log'
    formatter = logging.Formatter(
        fmt='%(asctime)s - %(levelname)s - %(module)s - %(message)s')
    loggerName = "{}".format(name)
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    logger = logging.getLogger(loggerName)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    return logger