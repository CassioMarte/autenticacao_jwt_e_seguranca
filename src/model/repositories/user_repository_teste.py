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


## teste uni
from unittest.mock import Mock

class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_repository():
    username = "fred"
    password = "Yabadabadoo"

    mock_connection = MockConnection()
    repo = UserRepository(mock_connection)

    repo.register_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)

