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
  "Pre-K": "i116",
  "pre-K": "i116",
  "Kindergarten": "i119",
  "kindergarten": "i119",
  "K": "i119",
  "k": "i119",
  "1": "i122",
  "2": "i125",
  "3": "i128",
  "4": "i131",
  "5": "i134",
  "6": "i137",
  "7": "i140",
  "8": "i143"
}

#A CSV file is open and it reads data from the file
with open('data.csv', 'r') as file:
    attendance = csv.reader(file)
    # Skip the header row
    next(attendance)
    for row in attendance:
        #ignores the name and the branch because that is unnecessary
        check = driver.find_element(By.CLASS_NAME, 'd7L4fc bJNwt  FXLARc aomaEc ECvBRb')
        check.click()
        name,date, school_name, grade, unique, math, ela, science, social_studies, other  = row[:]

        #branch is already chosen
       
        month, day = date.split("/") #there is no input for year
        month = month.zfill(2)
        day = day.zfill(2)
        total_date = month+'/'+day+'/'+'2023'

        
        #inputs the month and the day and the year
        date_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input')
        date_input.send_keys(total_date)

        #input school name
        school_name_input = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        school_name_input.send_keys(school_name)


        grade_options = driver.find_element(By.ID, grade_id[grade])
        grade_options.click()

        unique_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div') #done
        if (unique != "") and (unique[0] == 'Y' or unique[0] == 'y'):
            unique_.click()

        math_choice = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div') #done
        if (math != "") and (math[0] == 'Y' or math[0] == 'y'):
            math_choice.click()

        ela_choice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div/span/div/div/label')  #done
        if (ela != "") and (ela[0] == 'Y' or ela[0] == 'y'):
            ela_choice.click()

        science_choice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div/span/div/div/label/div/div[1]/div/div[3]/div')
        if (science != "") and (science[0] == 'Y' or science[0] == 'y'):
            science_choice.click()

        social_studies_choice = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div/span/div/div')
        if (social_studies != "") and (social_studies[0] == 'Y' or social_studies[0] == 'y'):
            social_studies_choice.click()

        other_ = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div/span/div/div')
        if other != "" and other != "no" and other != "No":
            other_.click()

        other_for_name = driver.find_element(By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea')
        other_for_name.send_keys(name)

        submit = driver.find_element(By.CLASS_NAME, 'NPEfkd RveJvd snByac')
        submit.click()

        another_form = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a[2]')
        another_form.click()

