from os.path import join
from src.parser import Parser

# questa funzione controlla se esiste una variabile d'ambiente associata al nome, 
# oppure un argomento passato da linea di comando, altrimenti, ritorna il valore di default
def check_if_arg(name, args, default):
    if args!= None and args[name] != None:
        return args[name]
    return default

parser = Parser()
args = parser.arguments()

# Path
BASE_LOG_PATH = check_if_arg("logpath", args, "")
LOG_PATH = join(BASE_LOG_PATH, "debug.log")
ERROR_LOG_PATH = join(BASE_LOG_PATH, "error.log")
CROMEDRIVER_PATH = check_if_arg("chromedriverpath", args, "chromedriver.exe")

# Credentials
USERNAME = check_if_arg("password", args, "")
PASSWORD = check_if_arg("username", args, "")

# Pages 
LOGIN_PAGE = "https://www.instagram.com/accounts/login/?hl=it"
INSTAGRAM_PAGE = "https://www.instagram.com/instagram/?hl=it"

# Server
SERVER_IP = "161.97.173.214"
SERVER_PORT = "80"
SERVER_URL = f"http://{SERVER_IP}:{SERVER_PORT}"

# Options
HEADLESS = True
DRIVER = 