# Import pandas
import os
import pandas as pd
from getpass import getpass, getuser
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
import log_cases_library


print('Enter file name (default: cases.csv):')
file_name = input()
if file_name == '':
    file_name = 'cases.csv'    
df = pd.read_csv(file_name)
opt = webdriver.ChromeOptions()
print('Username:')
uname = input()
pword = getpass()


# Open Chrome and log in
chromedriver_autoinstaller.install()
driver = webdriver.Chrome(options=opt)
driver.get('https://apps.acgme.org/ads/CaseLogs/CaseEntry/Insert')
username = driver.find_element(By.ID, "UserName")
username.send_keys(uname)
password = driver.find_element(By.ID, "Password")
password.send_keys(pword)
driver.find_element(By.XPATH, '//*[@id="signIn-link"]').click()


# from importlib import reload
# reload(log_cases_library)
# from log_cases_library import insert_case
# msg = log_cases_library.insert_case(df.iloc[1], driver)

for index, row in df.iterrows():
     print(row)
     try:
         msg = log_cases_library.insert_case(row, driver)
     except Exception as e:
         msg = str(e)
     df.at[index, 'Message'] = msg
     print(msg)
    
# Write the dataframe to a csv
df
df.to_csv('cases_out.csv', index=False)
