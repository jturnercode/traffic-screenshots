from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from PIL import ImageDraw, Image
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

    newfile_path = f'{img_dir}/{dtime}_{location["name"]}.png'
    driver.save_screenshot(newfile_path)

    # add datetime to image
    img = Image.open(newfile_path)
    I1 = ImageDraw.Draw(img)
    I1.text((30, 40), dtime, fill=(255, 0, 0))

    # Display edited image, for testing
    # img.show()

    # Save the edited image
    img.save(newfile_path)


# driver.close() is only for browser windows
# driver quit() should be used when done to properly
#  terminate all processes
driver.quit()
