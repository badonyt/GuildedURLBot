# Selenium Import
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# Random Stuff import
import random
import time
import json
# Class for colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Opens json file
data = json.load(open('Password.json'))
# Intructions
print(bcolors.OKCYAN + "You will have to press the Login button to enter. Since its bot protected" + bcolors.ENDC)
# Sees what browser the user wants
username = input("Enter Browser(recomended Firefox):")
if username == "Firefox" or username == "firefox":
    driver = webdriver.Firefox()
elif username == "Chrome" or username == "chrome":
    driver = webdriver.Chrome()
elif username == "Google" or username == "google":
    driver = webdriver.Chrome()
else:
    driver = webdriver.Firefox()
# gets guilded url
driver.get('https:/guilded.gg')

# gets password, email
username_CONST = data["Email"]
password_CONST = data["Password"]
# gets words that user wannts
url_const = ["bad", "nice", "cool","skeppy","andrewtate", "kkkkklllaosda"]
# Final button xpath
buttonfinal = "/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/div/div[1]/div/div/div/div[1]/div[2]/div[1]/button"
# Click Login Button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[1]/div/div/div[1]/div/button"))).click()
# Enter Email
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Email"))).send_keys(username_CONST)
# Enter password
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Password"))).send_keys(password_CONST)
# random debbuging not even sure why this is here
print(random.uniform(10, 15))
# sleeps for a bit so page loads and user has time to click the button
time.sleep(random.uniform(5,7))
driver.get("https://www.guilded.gg/profile/4vjDr6k4")
# Clicks settings button
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div/div/div[2]/div[2]/div"))).click()
#   Random Click?
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div[1]/div[1]/div[2]/div[2]/span/div[1]/div/div[1]/div/div/div/div[2]/div/div/div[2]/button"))).click()



def finalpart(wht):
    # debugs
    print(wht)
    # convenience purpose
    current_urr = wht
    # gets browser, because Chrome doesnt support deleting everything in one go
    if username == "Chrome" or username == "chrome" or username == "google" or username == "Google":
        for i in range(50):
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "URL"))).send_keys(Keys.BACKSPACE)
    else: 
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "URL"))).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "URL"))).clear()
    # Sends the keys
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "URL"))).send_keys(url_const[current_urr])
    # Server ussualy takes time to respond
    time.sleep(1.556)
    # Clicks button if possible
    try:
        if driver.find_element(By.XPATH, buttonfinal).is_enabled() == True:
            driver.find_element(By.XPATH, buttonfinal).click()
            time.sleep(3)
            driver.quit()
            return "0 STOP"
        else:
            print("The url isnt available, or something else.")
    except:
        print("ERROR, you have probably inputted your own URL") 
    # So next time it goes into the other part of the list
    current_urr += 1
    # Debugging
    print("cur url: " +  str(current_urr))
    print("url_const " + str(len(url_const)))
    # see if it is the same value, then resets it 
    if current_urr == int(len(url_const)):
        current_urr = 0
    # Calls it again
    finalpart(wht=current_urr)
# Calls it for the first time
finalpart(wht=0)
        

time.sleep(3)
driver.quit()
