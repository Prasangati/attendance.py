import csv
from selenium import webdriver
import time 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

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

grade_id = {              # identifies the id based on the grade  
  "Pre-K": "i123",
  "Kindergarten": "i126",
  "1": "i129",
  "2": "i132",
  "3": "i135",
  "4": "i138",
  "5": "i141",
  "6": "i144",
  "7": "i147",
  "8": "i150"
}

#A CSV file is open and it reads data from the file
with open('data.csv', 'r') as file:
    attendance = csv.reader(file)
    # Skip the header row
    next(attendance)
    for row in attendance:
        #ignores the name and the branch because that is unnecessary

        name,date, school_name, grade, unique, math, ela, science, social_studies, other  = row[0:]
        verify = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
        verify.click()
        #branch is already chosen
        element = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/span/div/div[6]/label/div/div[1]/div/div[3]/div')
        element.click()
        month, day = date.split("/") #there is no input for year
        month = month.zfill(2)
        day = day.zfill(2)
        total_date = month+'/'+day+'/'+'2023'

        
        #inputs the month and the day and the year
        date_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        date_input.send_keys(total_date)

        #input school name
        school_name_input = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div[1]/div/div[1]/input')
        school_name_input.send_keys(school_name)


        grade_options = driver.find_element(By.ID, grade_id[grade])
        grade_options.click()


        unique_ = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div1') #done
        if unique == 'Yes' or unique == 'yes':
            unique_.click()

        math_choice = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div') #done
        if math == 'Yes' or math == 'yes':
            math_choice.click()

        ela_choice = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div')  #done
        if ela == 'Yes' or ela == 'yes':
            ela_choice.click()

        science_choice = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div')
        if science == 'Yes' or science == 'yes':
            science_choice.click()

        social_studies_choice = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div')
        if social_studies == 'Yes' or social_studies == 'yes':
            social_studies_choice.click()

        other_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div/div')
        if other != "" and other != "no" and other != "No":
            other_.click()

        other_for_name = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div/div[1]/div[2]/textarea')
        other_for_name.send_keys(name)


        submit = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
        submit.click()

        another_link = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
        another_link.click()
        


