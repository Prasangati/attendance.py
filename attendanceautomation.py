from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)



# Navigate to the Google sign-in page
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdgh6hUBkUe99r3BoNEPnDDxo5kMUjl-PoRenbOz_Y-xAVOsA/viewform'
driver.get(url)
sleep(45) #sign in manually


branch = driver.find_element('//*[@id="i65"]/div[3]/div/div')





