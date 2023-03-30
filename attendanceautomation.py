import csv
from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import google.auth.exceptions

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome('drivers/chromedriver.exe', chrome_options=chrome_options)



# Navigate to the Google sign-in page
url = 'https://docs.google.com/forms/d/e/1FAIpQLSdgh6hUBkUe99r3BoNEPnDDxo5kMUjl-PoRenbOz_Y-xAVOsA/viewform'
email = "prasangatiwari@nypl.org"
password = "Ibrabest10-"
driver.get(url)
driver.implicitly_wait(10)  #Wait until the program loads

#Logs into the gmail account of your choice
email_input = driver.find_element(By.NAME, 'identifier')
email_input.send_keys(email)
email_input.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
password_input = driver.find_element(By.NAME,'Passwd' )
password_input.send_keys(password)
password_input.send_keys(Keys.RETURN)
time.sleep(30)

#A CSV file is open and it reads data from the file
with open('data.csv', 'r') as file:
    attendance = csv.reader(file)
    # Skip the header row
    next(attendance)
    for row in attendance:
        #ignores the name and the branch because that is unnecessary
        date, school_name, grade, unique, math, ela, science, social_studies, other  = row[1:]

        #branch is already chosen
        element = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div/span/div/div[21]/label/div/div[2]/div/span')
        element.click()
        month, day = date.split("/") #there is no input for year
        
        #inputs the month and the day and the year
        month_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
        month_input.send_keys(month)
        day_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div/div[1]/input')
        day_input.send_keys(day)
        year_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[5]/div/div[2]/div[1]/div/div[1]/input')
        year_input.send_keys('2023') #assumining it is all from 2023


        school_name_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        school_name_input.send_keys(school_name)


        select_grade = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[5]/div')
        grade_options = select_grade.find_elements(By.TAG_NAME, f'.//div[@data-value="{grade}"]')
        if grade_options:          #click the grade that matches what is given
            grade_options[0].click()

        unique_ = driver.find_element(By.XPATH, '//*[@id="i152"]/div[3]/div') #done
   
        math_choice = driver.find_element(By.XPATH, '//*[@id="i159"]/div[3]/div') #done
        ela_choice = driver.find_element(By.XPATH, '//*[@id="i166"]/div[3]/div/div')  #done
        science_choice = driver.find_element(By.XPATH, '//*[@id="i173"]/div[3]/div')
        social_studies = driver.find_element(By.XPATH, '//*[@id="i180"]/div[3]/div')
        other_ = driver.find_element(By.XPATH, '//*[@id="i187"]/div[3]/div')

        

