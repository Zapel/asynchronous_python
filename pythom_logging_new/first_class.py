import logging

class FirstClass:
    def __init__(self):
        self.current_number = 0
        self.logger = logging.getLogger(__name__)

    def increment_number(self):
        self.current_number += 1
        self.logger.warning('Число увеличивается!')
        self.logger.info('Число еще увеличивается!!')

    def decrement_number(self):
        self.current_number -= 1

    def clear_number(self):
        self.current_number = 0
        self.logger.warning('Очистка значения!')
        self.logger.info('Значение еще не очищено!!')