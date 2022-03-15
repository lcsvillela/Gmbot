from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from time import sleep
import datetime


class Gmbot:
    def __init__(self, username, password, classroom):
        self.__class = {
            "es": "https://meet.google.com/vri-bkgf-cyj",
            "redes": "meet.google.com/fvq-nwpr-cvu",
            "atp": "meet.google.com/scd-drpq-qon",
        }

        self.__username = username
        self.__password = password
        self.__classroom = classroom
        self.__links = {
            "login": "https://accounts.google.com/signin",
            "class": self.__classroom,
        }
        self.__location = {
            "username": "identifier",
            "password": "password",
            "button_login": '//*[contains(text(),"Próxima")]',
        }
        self.__driver = webdriver.Firefox()
        self.__wait = WebDriverWait(self.__driver, 30)
        self.__actions = ActionChains(self.__driver)
        self.start()

    def login(self):
        self.__driver.get(self.__links["login"])
        user = self.__driver.find_element_by_name(self.__location["username"])
        user.send_keys(self.__username)
        button = self.__driver.find_element_by_xpath(self.__location["button_login"])
        button.click()
        sleep(5)
        password = self.__driver.find_element_by_name(self.__location["password"])
        password.send_keys(self.__password)
        button = self.__driver.find_element_by_xpath(self.__location["button_login"])
        button.click()
        self.__driver.get(self.__classroom)
        sleep(1)
        action = ActionChains(self.__driver)
        action.key_down(Keys.CONTROL)
        action.send_keys("e")
        action.send_keys("d")
        action.key_up(Keys.CONTROL)
        action.perform()
        sleep(5)
        self.__driver.execute_script(
            "document.querySelectorAll(\"[role='button']\")[4].click()"
        )

    def verify(self):
        result = 7
        try:
            while result > 4:
                vector = self.__driver.page_source.split(" ")
                position = vector.index("pessoas</div></div><div")
                result = int(vector[position - 1])
                sleep(4)
                print(result + " " + datetime.datetime.now())
        except:
            self.__driver.close()

    def get_driver(self):
        return self.__driver

    def start(self):
        try:
            self.login()
            sleep(20)
            self.verify()
        except:
            self.__driver.close()
