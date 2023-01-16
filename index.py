import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import urllib.request
from lxml import etree
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
driver.get('https://akademik.itb.ac.id/app/K/mahasiswa:16322294+2022-2/kelas/jadwal/mahasiswa')                                         # Got to web
driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/a').click()                                             # Click login button
driver.find_element('xpath', '//*[@id="username"]').send_keys(nim)                                                                      # Send username
print('Inputted username')
driver.find_element('xpath', '//*[@id="password"]').send_keys(passwd)                                                                   # Send password
print('Inputted password')
driver.find_element('xpath', '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div/main/div/div[1]/div/div[2]/form/input[4]').click()    # Click login button
if check_exists_by_xpath("//*[contains(text(), 'Jadwal Perkuliahan Mahasiswa')]"):
    print('Login successful')
    # Search for the lecture
    hour = str(datetime.datetime.now().strftime('%H'))
    lecture = f"{hour}:00-"
    classes = driver.find_elements('xpath', f'//*[contains(text(), "{lecture}" )]')
    for i in classes:
        i.click()
        time.sleep(2.5)
        if check_exists_by_xpath('//*[@id="form_hadir"]'):
            break
        else:
            remove_element('/html/body/div[2]')
    print('Lecture found')
    # JUST FUCKING CLICK THE BUTTON KURWA
    driver.find_element('xpath', '//*[@id="form_hadir"]').click()
else:
    print('Login failed')
    