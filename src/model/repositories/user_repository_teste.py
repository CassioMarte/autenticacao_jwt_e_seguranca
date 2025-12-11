from unittest.mock import Mock
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


class MockCursor:
    def __init__(self) -> None:
        self.execute = Mock()
        self.fetchone = Mock()


class MockConnection:
    def __init__(self) -> None:
        self.cursor = Mock(return_value=MockCursor())
        self.commit = Mock()


def test_register_user():
    username = "fred"
    password = "Yabadabadoo"

    mock_connection = MockConnection()
    ##  repo = PetRepositories(cast(DBConnectionHandler, db_connection_mock))
    repo = UserRepository(mock_connection) # type: ignore

    repo.register_user(username, password)

    cursor = mock_connection.cursor.return_value

    assert "INSERT INTO users" in cursor.execute.call_args[0][0]
    assert "(username, password, balance)" in cursor.execute.call_args[0][0]
    assert "VALUES" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (username, password, 0)


def test_edit_balance():
    user_id = 1
    new_balance = 100.10

    mock_connection = MockConnection()
    repo =  UserRepository(mock_connection) # type: ignore

    repo.edit_balance(user_id, new_balance)

    cursor = mock_connection.cursor.return_value

    # print("###############")
    # print(cursor)
    # ## <src.model.repositories.user_repository_teste.MockCursor object at 0x7a200226f9e0>
    # print("###############")
    
    # call('\n              UPDATE users\n              SET\n              balance = ?\n              where id = ?;\n            ', (100.1, 1))
    assert 'UPDATE users' in cursor.execute.call_args[0][0]
    assert 'balance' in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (100.1, 1)

    # IMPORTANTE  - testar o commit
    mock_connection.commit.assert_called_once()
    

def test_get_user_by_user_name():
    user_name = 'Teste'

    mock_connection = MockConnection()

    repo = UserRepository(mock_connection) # type: ignore

    repo.get_user_by_user_name(user_name)

    cursor = mock_connection.cursor.return_value

    assert "SELECT" in cursor.execute.call_args[0][0]
    assert "id, username, password" in cursor.execute.call_args[0][0]
    assert cursor.execute.call_args[0][1] == (user_name, )

    # importante
    cursor.fetchone.assert_called_once()

