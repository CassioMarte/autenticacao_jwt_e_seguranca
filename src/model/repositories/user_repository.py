from .user_repository_interface import UserRepositoryInterface
from sqlite3 import Connection

class UserRepository(UserRepositoryInterface):
    def __init__(self, conn: Connection)-> None:
        self.__conn = conn

    def register_user(self, user_name: str, password: str)-> None:
        cursor = self.__conn.cursor()

        cursor.execute('''INSERT INTO users 
                           (username, password, balance) 
                        VALUES
                           (?, ?, ?);
                       ''',
                       (user_name, password, 0)
                       )
        
        self.__conn.commit()
