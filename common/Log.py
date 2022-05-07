


import logging
import os.path


def log():
    log_dir = os.path.dirname(os.path.dirname(__file__)) + "\\Log\\test.log"
    # 设置log基础配置信息(级别level，格式format)
    logging.basicConfig(filename=log_dir,level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')
    # 定义日志名称，在输出日志时显示
    logger = logging.getLogger('log_test')
    return logger
logger = log()
if __name__ == '__main__':
    logger.info('info信息')
    logger.debug('debug信息')
    logger.warning('warning信息')
    logger.critical('critical信息')
