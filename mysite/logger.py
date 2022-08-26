import logging
import logging.handlers
import time
import configparser
from getRoot import get_root


class myLogger(object):

    def __init__(self, log):
        print(get_root())
        config = configparser.ConfigParser()
        file_path = get_root() + '/config/config.ini'
        config.read(file_path)
        self.logger = logging.getLogger(log)
        if config['log']['level'] == 'DEBUG':
            level = logging.DEBUG
        elif config['log']['level'] == 'INFO':
            level = logging.INFO
        self.logger.setLevel(level)
        rq = time.strftime('%Y%m%d', time.localtime(time.time()))
        log_path = get_root() + '/logs/'
        log_name = log_path + rq + '.log'
        fh = logging.handlers.RotatingFileHandler(log_name, maxBytes=1024 * 1024,
                                                 backupCount=5, encoding='utf-8')
        fh.setLevel(level)
        ch = logging.StreamHandler()
        ch.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def get_log(self):
        return self.logger
