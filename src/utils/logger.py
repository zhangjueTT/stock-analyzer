import logging

class Logger(object):

    def __init__(self):
        logging.basicConfig(level=logging.DEBUG,  # 控制台打印的日志级别
                            # filename='temp/logs/2019-11-12.log',
                            filemode='a',
                            format=
                            '%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s'
                            )

    @staticmethod
    def debug(tag, msg):
        logging.debug("[" + tag + "] " + msg)

    @staticmethod
    def info(tag, msg):
        logging.info("[" + tag + "] " + msg)

    @staticmethod
    def warn(tag, msg):
        logging.warning("[" + tag + "] " + msg)

    @staticmethod
    def error(tag, msg):
        logging.error("[" + tag + "] " + msg)

logger = Logger()
