from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "/Users/rafael/Downloads/chromedriver_mac64"
service = Service(executable_path=chrome_driver)

#time = time.time()
timeout = time.time() + 5

with webdriver.Chrome(service=service) as driver:
    driver.get("http://orteil.dashnet.org/experiments/cookie/")
    cookie = driver.find_element(By.ID, "cookie")

    while True:
        buy_cursor = driver.find_element(By.ID, "buyCursor")
        buy_grandma = driver.find_element(By.ID, "buyGrandma")
        buy_factory = driver.find_element(By.ID, "buyFactory")

        if time.time() >= timeout:
            money = driver.find_element(By.ID, "money")
            if int(money.text) >= 500:
                buy_factory.click()
            elif int(money.text) >= 100:
                buy_grandma.click()
            else:
                buy_cursor.click()
            timeout = time.time() + 5
        else:
            cookie.click()


    # for n in range(1,16):
    #     cookie.click()
    # time.sleep(3)
    # cursor_button = driver.find_element(By.ID, "buyCursor")
    # cursor_button.click()
    # time.sleep(3)
    # for n in range(1,101):
    #     cookie.click()
    # time.sleep(3)