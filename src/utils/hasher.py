
import hashlib


def file_token(name_token: str, pass_token: str) -> str:
    file_hash = pass_token + name_token * 2
    file_hash = hashlib.sha3_256(file_hash.encode('utf-8')).hexdigest()
    return file_hash


def password_hash(password: str) -> str:
    password = password * (len(password) + 2)
    pass_hash = hashlib.sha3_256(password.encode('utf-8')).hexdigest()
    return pass_hash


def username_hash(username: str) -> str:
    username = username * (len(username) + 3)
    name_hash = hashlib.sha3_256(username.encode('utf-8')).hexdigest()

    return name_hash

