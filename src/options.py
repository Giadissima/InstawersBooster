from src.costants import HEADLESS

from selenium.webdriver.chrome.options import Options

# Instants Chrome driver
options = Options()
options.headless = HEADLESS
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
options.add_argument("--log-level=3")

DRIVER = webdriver.Chrome("chromedriver.exe", options=options)