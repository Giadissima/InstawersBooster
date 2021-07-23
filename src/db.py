import requests
from src.costants import SERVER_URL, USERNAME

def get_auth():
    return requests.get(SERVER_URL, params = {"username":USERNAME})