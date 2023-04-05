import jwt
from models.user import User


# Token generator
def token_generator(email):
    key = 'secret'
    encoded = jwt.encode({'profile..': email}, key, algorithm='HS256')
    return encoded


# Add 'hashed_password' to user
class UserInDB(User):
    hashed_password: str


# decode
def decode_token(token):
    try:
        decode = jwt.decode(token, key='secret', algorithms=['HS256', ])
        print(decode)
        return decode
    except jwt.InvalidSignatureError:
        # todo: return descriptive error
        raise ValueError('')
    except jwt.DecodeError:
        # todo: return descriptive error
        raise ValueError('')
