# from os import path, remove
# import logging
# import logging.config
#
# from .first_class import FirstClass
# from .second_class import SecondClass
#
# # Удалите существующий файл лога, если он есть, чтобы создавать новый файл во время каждого выполнения
# if path.isfile("python_logging.log"):
#     remove("python_logging.log")
#
# # Создайте Logger
# logger = logging.getLogger(__name__)
# logger.setLevel(logging.INFO)
#
# # Создайте обработчик для записи данных в файл
# logger_handler = logging.FileHandler('python_logging.log')
# logger_handler.setLevel(logging.INFO)
#
# # Создайте Formatter для форматирования сообщений в логе
# logger_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
#
# # Добавьте Formatter в обработчик
# logger_handler.setFormatter(logger_formatter)
#
# # Добавте обработчик в Logger
# logger.addHandler(logger_handler)
# logger.info('Настройка логгирования окончена!')

from os import path, remove
import logging
import logging.config
import json

from .first_class import FirstClass
from .second_class import SecondClass

# Удалите существующий файл лога, если он есть, чтобы создавать новый файл во время каждого выполнения
if path.isfile("python_logging.log"):
    remove("python_logging.log")

with open("python_logging_configuration.json", 'r') as logging_configuration_file:
    config_dict = json.load(logging_configuration_file)

logging.config.dictConfig(config_dict)

# Запись о том, что logger настроен
logger = logging.getLogger(__name__)
logger.info('Настройка логгирования окончена!')