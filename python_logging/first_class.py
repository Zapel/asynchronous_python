import logging

class FirstClass:
    def __init__(self):
        self.current_number = 0
        # Создайте Logger
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)

        # Создайте обработчик для записи данных в файл
        logger_handler = logging.FileHandler('python_logging.log')
        logger_handler.setLevel(logging.INFO)

        # Создайте Formatter для форматирования сообщений в логе
        logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')

        # Добавьте Formatter в обработчик
        logger_handler.setFormatter(logger_formatter)

        # Добавте обработчик в Logger
        self.logger.addHandler(logger_handler)
        self.logger.info('Настройка логгирования окончена!')

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