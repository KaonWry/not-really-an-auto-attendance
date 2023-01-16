import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Firefox()

# Authentication
f = open('auth.txt', 'r')
nim = f.readline()
passwd = f.readline()

# Check if an element exists
def check_exists_by_xpath(xpath):
    try:
        driver.find_element('xpath', xpath)
    except NoSuchElementException:
        return False
    return True

# Remove an element
def remove_element(xpath):
    element = driver.find_element('xpath', xpath)
    driver.execute_script("""
    var element = arguments[0];
    element.parentNode.removeChild(element);
    """, element)

# Login
driver.get(f'https://akademik.itb.ac.id/app/K/mahasiswa:{nim}/kelas')                                         # Got to web
driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/a').click()                                             # Click login button
driver.find_element('xpath', '//*[@id="username"]').send_keys(nim)                                                                      # Send username
print('Inputted username')
driver.find_element('xpath', '//*[@id="password"]').send_keys(passwd)                                                                   # Send password
print('Inputted password')
driver.find_element('xpath', '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div/main/div/div[1]/div/div[2]/form/input[4]').click()    # Click login button
if check_exists_by_xpath("//*[contains(text(), 'Jadwal Perkuliahan Mahasiswa')]"):
    print('Login successful')
    # Search for the lecture
    hour = str(datetime.datetime.now().strftime('%H'))      # The real deal
    # hour = str(7)                                         # Testing purposes
    lecture = f"{hour}:00-"
    attend = driver.find_elements('xpath', f'//*[contains(text(), "{lecture}" )]')
    # Bruteforce all classes in the same hour to search for that one attendance button
    for i in attend:
        i.click()
        try:
            element_present = EC.presence_of_element_located((By.XPATH , '/html/body/div[2]/div[2]/div/div/div/div/div/div/div/div[4]/button'))
            WebDriverWait(driver, 3).until(element_present)
        except TimeoutException:
            print ("Loading took too much time!")
            remove_element('/html/body/div[2]')
            continue            
        if check_exists_by_xpath('//*[@id="form_hadir"]'):
            break
        else:
            remove_element('/html/body/div[2]')
    print('Lecture found')
    # JUST FUCKING CLICK THE BUTTON KURWA
    driver.find_element('xpath', '//*[@id="form_hadir"]').click()
else:
    print('Login failed')