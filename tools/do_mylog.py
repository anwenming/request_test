import logging

class My_Logger:

    def my_loge(self,msg,leave):
        #设定日志收集器
        my_logger=logging.getLogger('python11')
        #设定级别
        my_logger.setLevel('DEBUG')

        formatter=logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        # 输出渠道
        ch =logging.StreamHandler()
        ch.setLevel('DEBUG')
        ch.setFormatter(formatter)

        # 创建输出渠道
        fh =logging.FileHandler('API.txt',encoding='utf-8')
        fh.setLevel('INFO')
        fh.setFormatter(formatter)
        # 指定输出渠道
        my_logger.addHandler(ch)
        my_logger.addHandler(fh)

        if leave == 'DEBUG':
            my_logger.debug(msg)
        elif leave == 'INFO':
            my_logger.info(msg)
        elif leave == 'ERROR':
            my_logger.error(msg)
        elif leave == 'WARNING':
            my_logger.warning(msg)
        elif leave == 'CRITICAL':
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self,msg):
        self.my_loge(msg,'DEBUG')

    def info(self,msg):
        self.my_loge(msg,'INFO')

    def error(self,msg):
        self.my_loge(msg,'ERROR')

    def warning(self,msg):
        self.my_loge(msg,'WARNING')

    def critical(self,msg):
        self.my_loge(msg,'CRITICAL')



if __name__ == '__main__':
    my_Log=My_Logger()
    my_Log.warning('有问题')
    my_Log.info('写进去')
    my_Log.critical('显示出来吧')
