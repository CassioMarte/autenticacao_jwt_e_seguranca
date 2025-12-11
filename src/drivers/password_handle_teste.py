from .password_handler import PasswordHandler

def test_encrypt_password():
    my_pass = "123456"

    handle = PasswordHandler()

    hashed = handle.encrypt_password(my_pass)

    print("###################")
    print("res: ", hashed)


def test_check_password():
    hash =  b'$2b$12$1Q0jrD2ecmVRzvEcNjkbvulMvCnPYVd1Bo8C2sOTE7uKEOYj912yq'
    
    handle = PasswordHandler()

    decod = handle.check_password("123456",  hash) # type: ignore

    print("###################")
    print("res: ", decod)