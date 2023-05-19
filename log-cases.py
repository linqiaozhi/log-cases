
# Import pandas
import pandas as pd
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


opt = webdriver.ChromeOptions()
# opt.add_argument("--start-maximized")

chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)
driver.get('https://stackoverflow.com/')


service_object = Service(binary_path)
driver = webdriver.Chrome(service=service_object)

file_path = '/Users/george/Downloads/cases.csv'
# Load the file named test.csv using pandas
df = pd.read_csv(file_path)
# First row
df.iloc[1]

#Log in
driver = webdriver.Chrome(...)  # Or Chrome(), or Ie(), or Opera()

# To catch <input type="text" id="passwd" />
password = driver.find_element(By.ID, "passwd")
# To catch <input type="text" name="passwd" />
password = driver.find_element(By.NAME, "passwd")

password.send_keys("Pa55worD")

driver.find_element(By.NAME, "submit").click()


