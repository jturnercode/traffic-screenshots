from time import sleep
from os import getenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# setup webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")

# uses set screen resolution on the machine if headless is off
# options.add_argument("--window-size=1920x1080")
options.add_argument("--window-size=800x600")

# options.add_argument("--start-maximized")  # Do NOT USE IN HEADLESS MODE
driver = webdriver.Chrome(options=options, service=Service(getenv("CHROMEDRIVER")))

driver.implicitly_wait(8)

# Brazos Event area
driver.get(getenv("BRAZOS_URL"))
driver.save_screenshot("Brazos.png")

# 99/59
driver.get(getenv("99_URL"))
driver.save_screenshot("9959.png")

# sleep(8)
driver.close()
