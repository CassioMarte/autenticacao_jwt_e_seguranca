from src.model.setting.db_connection_handle import db_connection_handle
from .user_repository import UserRepository
## Teste de conexão 

def teste_repository():
    db_connection_handle.connect() 
    conn = db_connection_handle.get_connection()

    repo = UserRepository(conn)

    user_name = "Fulano de tal"
    password = "123456"

    repo.register_user(user_name, password)
     
    user = repo.get_user_by_user_name(user_name)
     
    print("##############")
    print(user)
    print("##############")

    repo.edit_balance(user[0], 100.00)

    user_with_balance = repo.get_user_by_user_name(user_name)
    
    print("##############")
    print(user_with_balance)
    print("##############")

    


 

## Teste unitarios

