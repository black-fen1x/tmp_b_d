import logging
import os

log_dir = 'logs'
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Хендлер для сохранения логов в файл
log_file = os.path.join(log_dir, 'bot.log')
file_handler = logging.FileHandler(log_file)

#Настройка формата лога
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


"""
Для импорта логгера использовать следующий код:
import logging
from log_handler import logger

Пример лога:
logger.info('Новая запись в лог')
"""
