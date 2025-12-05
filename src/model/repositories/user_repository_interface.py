from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    
    def register_user(self, user_name: str, password: str)-> None:
        pass

    def edit_balance(self, user_id: int, new_balance:float)-> None:
        pass

    def get_user_by_user_name(self, user_name:str):
        pass