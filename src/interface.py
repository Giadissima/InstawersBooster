from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import (NoSuchElementException, TimeoutException, 
                                        WebDriverException)
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class is_clickable(object):
        def __init__(self, locator):
            self.locator = locator
        
        def __call__(self, driver):
            try:
                located = EC.presence_of_element_located(self.locator)(driver)
                clickable = EC.element_to_be_clickable(self.locator)(driver)
                if not located or not clickable:
                    return False
                return located
            except WebDriverException:
                return False

class Interface:
    def __init__(self, driver):
        # buttons to click
        self.XPATH_follow_button = "//button[text()=\"Segui\"]"
        self.XPATH_credentials_button = "//button[@type='submit' and contains(.,\"Accedi\")]"
        self.XPATH_cookies_button = "//button[contains(.,\"Accetta\")]"
        self.XPATH_notification_button = "//button[contains(.,\"Non ora\")]"
        self.XPATH_stop_to_follow_button = "//button[text()=\"Non seguire più\"]"
        self.CLASS_unfollow = "glyphsSpriteFriend_Follow"
        self.XPATH_too_attempts = "//p[text()=\"Attendi qualche minuto prima di riprovare.\"]"

        # credentials
        self.USERNAME = "icybix.boost"
        self.PASSWORD = ""

        self.followed = False
        self.driver = driver

    def check_if_followed(self):
        try:
            WebDriverWait(self.driver, 5).until(
                is_clickable((By.CLASS_NAME, self.CLASS_unfollow))
            )
            followed = True
        except (NoSuchElementException, TimeoutException):
            followed = False
        return followed

    def check_element(self, type, button):
        return WebDriverWait(self.driver, 10).until(
            is_clickable((type, button))
        )

    