from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config_mod import config as cfg

# setup webdriver
options = webdriver.ChromeOptions()
options.add_argument("headless")

# for testing, do not use w/headless mode
# options.add_argument("--window-size=1024x720")
# options.add_argument("--start-maximized")

# create driver instance
driver = webdriver.Chrome(options=options, service=Service(cfg["chromedriver"]))
driver.implicitly_wait(10)

# get locations set in .toml file
locations: list[dict] = cfg["locations"]
img_dir: str = cfg["img_dir"]

# datetime used to name .png file
dtime = datetime.now().strftime(r"%y%m%d_%H%M")

# iterate over locations and take snapshots
for location in locations:
    driver.set_window_size(**location["window"])
    driver.get(location["url"])
    driver.save_screenshot(f'{img_dir}/{dtime}_{location["name"]}.png')

driver.close()
