from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver = "/Users/rafael/Downloads/chromedriver_mac64"
service = Service(executable_path=chrome_driver)

digit = time.localtime()[5]
timeout = time.time() + 60

with webdriver.Chrome(service=service) as driver:
    driver.get("http://orteil.dashnet.org/experiments/cookie/")

    cookie = driver.find_element(By.ID, "cookie")

    while time.time() <= timeout:
        time.sleep(0.001)
        if time.localtime()[5] % 5 == 0:
            while int(driver.find_element(By.ID, "money").text) >= 15:
                money = driver.find_element(By.ID, "money").text
                buy_cursor = driver.find_element(By.ID, "buyCursor")
                buy_grandma = driver.find_element(By.ID, "buyGrandma")
                buy_factory = driver.find_element(By.ID, "buyFactory")
                buy_mine = driver.find_element(By.ID, "buyMine")
                buy_shipment = driver.find_element(By.ID, "buyShipment")
                buy_alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
                buy_portal = driver.find_element(By.ID, "buyPortal")
                buy_time_machine = driver.find_element(By.ID, "buyTime machine")
                buy_grandma = driver.find_element(By.ID, "buyGrandma")
                # i have to put the find_elements into while loop otherwise after second entered the while loop program crash
                # with find_element.click() error
                if int(money) >= 123456789:
                    buy_time_machine.click()
                    print("buy_time_machine.click()")
                elif int(money) >= 1000000:
                    buy_portal.click()
                    print("buy_portal.click()")
                elif int(money) >= 50000:
                    buy_alchemy_lab.click()
                    print("buy_alchemy_lab.click()")
                elif int(money) >= 7000:
                    buy_shipment.click()
                    print("buy_shipment.click()")
                elif int(money) >= 2000:
                    buy_mine.click()
                    print("buy_mine.click()")
                elif int(money) >= 500:
                    buy_factory.click()
                    print("buy_factory.click()")
                elif int(money) >= 100:
                    buy_grandma.click()
                    print("buy_grandma.click()")
                else:
                    buy_cursor.click()
                    print("buy_cursor.click()")
                time.sleep(0.1) # program crash without time.sleep()
        else:
            cookie.click()

        digit = time.localtime()[5]
