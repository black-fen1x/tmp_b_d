"""
Main bot configuration
01.02.2023
"""
import os

"""
Bot Variables
"""
tbot = os.getenv('BOT_TOKEN')

"""
DataBase Variables
"""
host = os.getenv('HOST_NAME_DB')
user = os.getenv('USER_NAME_DB')
password = os.getenv('PASSWORD_DB')
db_name = os.getenv('DB_NAME')
