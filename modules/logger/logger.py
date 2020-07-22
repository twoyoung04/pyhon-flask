''' wrapper around logging module '''
import os
import logging
import json
import json_log_formatter

def get_root_logger(logger_name, filename=None):
    ''' get the logger object '''
    debug = os.environ.get('ENV', 'development') == 'development'

    formatter = json_log_formatter.JSONFormatter()
    # formatter = json.dumps({
    #     "time": "%(asctime)s",
    #     "levelname": "%(levelname)s",
    #     "name": "%(name)s",
    #     "message": "%(message)s"
    # })

    log_handler = logging.StreamHandler()
    log_handler.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.addHandler(log_handler)
    logger.setLevel(logging.INFO)

    return logger