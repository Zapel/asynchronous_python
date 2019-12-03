import logging

class SecondClass(object):
    def __init__(self):
        self.enabled = False
        self.logger = logging.getLogger(__name__)

    def enable_system(self):
        self.enabled = True
        self.logger.warning('Включение системы!')
        self.logger.info('Система все еще включается!!')

    def disable_system(self):
        self.enabled = False
        self.logger.warning('Выключение системы!')
        self.logger.info('Система все еще выключается!!')
