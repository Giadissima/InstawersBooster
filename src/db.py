import requests

ip = "161.97.173.214"
porta = "80"

url = f"http://{ip}:{porta}"

def get_response(user):
    return requests.get(url, params = {"username":user})