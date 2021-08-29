from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.chrome.options import Options

from src.log import *
from src.interface import *
from src.exception import *
from src.file import *

from time import sleep
from random import SystemRandom
import os, traceback

from string import ascii_letters
from getpass import getpass

""" 
    This program can help you to boost your instagram followers.
    It consists on follow and unfollow a target with a large amount of followers: 
    in this way people will start to follow you to some funcking reason   """

def genRandString(lenght=10):
    return ''.join([SystemRandom().choice(ascii_letters) for _ in range(lenght)])

def clear():
   if os.name == "nt":
       os.system("cls")
   else:
        os.system("clear")

def main():
    # pages 
    LOGIN_PAGE = "https://www.instagram.com/accounts/login/?hl=it"
    INSTAGRAM_PAGE = "https://www.instagram.com/instagram/?hl=it"

    # instance to colors terminal
    log = ColoredPrint()

    # Chrome driver
    options = Options()
    options.headless = True
    options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36')
    options.add_argument("--log-level=3");
    driver = webdriver.Chrome("chromedriver.exe", options=options)
    i = Interface(driver)

    # instance of the main interface
    clear()
    # create an awesome and pink ascii art
    log.pink("""

    _          __                            __                 __         
   (_)__  ___ / /____ __    _____ _______   / /  ___  ___  ___ / /____ ____
  / / _ \(_-</ __/ _ `/ |/|/ / -_) __(_-<  / _ \/ _ \/ _ \(_-</ __/ -_) __/
 /_/_//_/___/\__/\_,_/|__,__/\__/_/ /___/ /_.__/\___/\___/___/\__/\__/_/   
                                                                        

""")
    # print and store time and username
    log.info("Ora di inizio: ", log.time(), "\neffettuato il login a: ", i.USERNAME)
    log.store()

    unfinished = True
    while unfinished:
        driver.implicitly_wait(10) # wait a maximum 10 seconds 
        # go to insta login page
        driver.get(LOGIN_PAGE)

        try:
            # find and click "accept cookies" button
            cookies_button = i.check_element(By.XPATH, i.XPATH_cookies_button)
            cookies_button.click()
            # print and log into a file
            log.success(log.time(), " cookie accettati")
            log.store()
        except (NoSuchElementException, TimeoutException) as e:
            log.warn(log.time(), " non sono riuscito ad accettare i cookie, proseguo.")
            log.store()
        
        try:
            # find login form
            user_form = i.check_element(By.NAME, "username")
            pssw_form = i.check_element(By.NAME, "password")
            # insert on login form username and password
            user_form.send_keys(i.USERNAME)

            notfinished = True

            while notfinished:
                try:
                    # caso i.password non è vuoto
                        #     chiede nuova password
                        #     chiede se vuoi salvarla
                        #         salva
                        #     effettua il login
                    saved_password = check_if_password_is_saved() 
                    if i.PASSWORD:
                        last_pass = len(i.PASSWORD)
                        for e in range(last_pass):
                            pssw_form.send_keys(Keys.BACKSPACE)
                        i.PASSWORD = None
                        saved_password = None

                    # caso i.password vuoto
                    #     controlla se esiste la password sul file:
                    #         chiede "vuoi utilizzare quella salvata?"
                    #     chiede nuova password
                    #     chiede se vuoi salvarla
                    #         salva
                    #     effettua il login
                    if saved_password:
                        risposta = ''
                        while risposta != 's' and risposta != 'n':
                            risposta = input("Utilizzare la password salvata? S/N\n").lower() 
                            if risposta == 's':
                                i.PASSWORD = saved_password
                            elif risposta != 'n':
                                log.err("Digita S o N per continuare")
                                log.store()
                    
                    save = False
                    if not i.PASSWORD:
                        print("inserisci la password, non verrà mostrata sullo schermo. Premi invio per confermare")
                        i.PASSWORD = getpass()
                        risposta = ''
                        while risposta != 's' and risposta != 'n':
                            risposta = input("Vuoi salvare la password? S/N\n").lower() 
                            if risposta == 's':
                                save = True
                            elif risposta != 'n':
                                log.err("Digita S o N per continuare")
                                log.store()
                    # error cases
                    if len(i.PASSWORD) < 6:
                        raise PasswordTooShort()
                    pssw_form.send_keys(i.PASSWORD)
                    # send form
                    credential_button = i.check_element(By.XPATH, i.XPATH_credentials_button)
                    credential_button.click()     
                    try: 
                        if driver.find_element_by_xpath(i.XPATH_too_attempts):
                            raise TooAttempts()  
                    except (NoSuchElementException, TimeoutException):
                        pass
                    notification_button = i.check_element(By.XPATH, i.XPATH_notification_button)
                    if save:
                        save_password_on_file(i.PASSWORD)
                        log.success("La password è stata salvata per gli usi futuri")
                        log.store()
                    # print and log into a file
                    log.success(log.time(), " credenziali inviate")
                    log.store()
                    notfinished = False
                except (NoSuchElementException, TimeoutException):
                    log.err("password incorretta, riprovare")
                    log.store()
                except PasswordTooShort:
                    log.err("La password deve avere minimo 6 caratteri, riprova")
                    log.store()
                except TooAttempts:
                    log.err("hai effettuato troppi tentativi, riprova tra qualche minuto")
                    log.store()

            # the notification button appears when page isn't load compleatly. 
            # We need to do a forced sleep althrought it doesn't works
            # sleep(3)
            # find and click notification button
            notification_button = i.check_element(By.XPATH, i.XPATH_notification_button)
            notification_button.click()        
            # print and log into a file
            log.success(log.time(), "pulsante notifica cliccato")
            log.store()
            unfinished = False
        # when browser doesn't find an element, log the error and exit
        except (NoSuchElementException, TimeoutException) as e:
            log.err(log.time(), "errore: controlla la tua connessione")
            driver.save_screenshot('img/last_error{}.png'.format(genRandString()))
            log.store()
            log.store_message("error.log","\n\n", traceback.format_exc(), "\n\n")

        except WebDriverException as e:
            msg = e.msg.split("\n")[0]
            if msg == 'chrome not reachable' or msg == 'unknown error: Chrome failed to start: was killed.':
                log.err(log.time(), "errore: il programma si è chiuso in modo inaspettato")
                sleep(3)
                exit()
            else:
                log.err(log.time(), "errore: si è verificato un errore sconosciuto")
                log.store_message("error.log","\n\n", traceback.format_exc(), "\n\n")
            log.store()
            log.store_message('error.log', "\n\n", msg, "\n\n")
        except Exception:
            log.err(log.time(), "errore: si è verificato un errore sconosciuto")
            log.store_message("error.log","\n\n", traceback.format_exc(), "\n\n")
            driver.save_screenshot('img/last_error{}.png'.format(genRandString()))
    
    driver.implicitly_wait(10) # wait a maximum 10 seconds 
    driver.get(INSTAGRAM_PAGE)
    followed = i.check_if_followed()

    while True:
        try:
            driver.execute_script("document.body.scrollTop = 0; document.documentElement.scrollTop = 0;")
            sleep(3)
            
            # if we're following the target, unfollow
            if followed:
                # find and click unfollow button
                unfollow_button = i.check_element(By.CLASS_NAME, i.CLASS_unfollow)
                unfollow_button.click()
                # print and log into a file
                log.success(log.time(), "unfollow button cliccato")
                log.store()
                # find and click stop to follow button
                stop_to_follow_button = i.check_element(By.XPATH, i.XPATH_stop_to_follow_button)
                stop_to_follow_button.click()
                # print and log into a file
                log.success(log.time(), "Non seguire piu button cliccato")
                log.store()
            # else follow the target and sleep a bit
            else:
                follow_button = i.check_element(By.XPATH, i.XPATH_follow_button)
                follow_button.click()
                log.success(log.time(), "follow button cliccato")
                log.store()
                # # create a random countdown between 90 and 120 seconds to avoid instagram's suspicious
                countdown = SystemRandom().randint(90, 120)
                sleep(countdown)
                # # print and log into a file
                log.warn(log.time(), "fine countdown")
                log.store()
            followed = not followed
                
        # when browser doesn't find an element, log the error
        except (NoSuchElementException, TimeoutException) as e:
            log.err(log.time(), "errore: controlla la tua connessione")
            driver.save_screenshot('img/last_error{}.png'.format(genRandString()))
            log.store_message("error.log","\n\n", traceback.format_exc(), "\n\n")
            driver.implicitly_wait(10) # wait a maximum 10 seconds             
            driver.get(INSTAGRAM_PAGE)
            followed = i.check_if_followed()
        
        except WebDriverException as e:
            msg = e.msg.split("\n")[0]
            if msg == 'chrome not reachable' or msg == 'unknown error: Chrome failed to start: was killed.':
                log.err(log.time(), "errore: il programma si è chiuso in modo inaspettato")
                sleep(3)
                exit()
            else:
                log.err(log.time(), "errore: si è verificato un errore sconosciuto")
            log.store()
            log.store_message('error.log', "\n\n", msg, "\n\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Good bye :)")
  