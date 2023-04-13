import psycopg2
from psycopg2 import Error

class DataBase:
    def __init__(self, host_name, user_name, user_password, db_name):
        try:
            self.connection = psycopg2.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = db_name
            )
            self.cursor = self.connection.cursor()
            self.connection.autocommit = True

        except (Exception, Error) as error:
            print('[ERROR] Error while working with PostgreSQL', error)

    def add_user(self, user_id, user_name):
         with self.connection:
            return self.cursor.execute("INSERT INTO users_id (user_id, user_name) VALUES (%s, %s)", (user_id, user_name))

    def user_exists(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT user_id FROM users_id WHERE user_id = (%s)", [user_id])
            result = self.cursor.fetchall()
            return bool(result)

    def set_group(self, user_id, user_group):
        with self.connection:
            self.cursor.execute("UPDATE users_id SET user_group = (%s) WHERE user_id = (%s)", (user_group, user_id))

    def get_signup(self, user_id):
        with self.connection:
            self.cursor.execute("SELECT signup FROM users_id WHERE user_id = (%s)", [user_id])
            result = self.cursor.fetchall()
            for row in result:
                signup = str(row[0])
            return signup

    def set_signup(self, user_id, signup):
        with self.connection:
            return self.cursor.execute("UPDATE users_id SET signup = (%s) WHERE user_id = (%s)", (signup, user_id))

    def change_group(self, user_id, user_group):
        with self.connection:
            return self.cursor.execute("UPDATE users_id SET user_group = (%s) WHERE user_id = (%s)", (user_group, user_id))

    def all_chat(self, user_group):
        self.cursor.execute("SELECT user_id FROM users_id WHERE user_group = %s", (user_group,))
        return (self.cursor.fetchall())

    def get_role(self, user_id):
         self.cursor.execute("SELECT admin_role FROM users_id WHERE user_id = %s", (user_id,))
         return (self.cursor.fetchall())
