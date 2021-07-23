import base64
from os.path import isfile

def save_password_on_file(password):
    password = base64.b64encode(password.encode("utf-8")).decode('utf-8')
    file = open("data.txt", "w")
    file.write(password)
    file.close()

def decode_pssw(encoded):
    return base64.b64decode(encoded).decode('utf-8')

def check_if_password_is_saved():
    if isfile("data.txt"):
        # File exist
        return decode_pssw(open("data.txt", "r").readline())
    else:
        # File not exist
        return None
