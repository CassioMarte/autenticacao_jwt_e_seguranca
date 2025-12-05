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

    def edit_balance(self, user_id: int, new_balance:float):
        cursor =  self.__conn.cursor()
        cursor.execute(
            '''
              UPDATE users
              SET
              balance = ?
              where id = ?;
            ''',
            (new_balance, user_id)
        )

        self.__conn.commit()

    def get_user_by_user_name(self, user_name:str):
        cursor = self.__conn.cursor()

        cursor.execute(
            '''
            SELECT 
              id, username, password
            FROM users
            WHERE username = ?;
            ''',
            (user_name, )
        )

        user = cursor.fetchone()
        return user

