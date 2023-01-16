import datetime
import time
from selenium import webdriver
import urllib.request
from lxml import etree
driver = webdriver.Firefox()

# Login
driver.get('https://akademik.itb.ac.id/app/K/mahasiswa:16322294+2022-2/kelas/jadwal/mahasiswa')                                         # Got to web
driver.find_element('xpath', '/html/body/div[1]/div[2]/div[1]/div/div[2]/div[2]/a').click()                                             # Click login button
driver.find_element('xpath', '//*[@id="username"]').send_keys('16322294')                                                               # Send username
print('Inputted username')
driver.find_element('xpath', '//*[@id="password"]').send_keys('Titan_2011')                                                             # Send password
print('Inputted password')
driver.find_element('xpath', '/html/body/div/div/div[2]/div/div[1]/div/div[2]/div/main/div/div[1]/div/div[2]/form/input[4]').click()    # Click login button
print('Login successful')

# Search for the lecture
day = str(datetime.datetime.now().strftime('%d'))
hour = str(datetime.datetime.now().strftime('%H'))
lecture = f"{hour}:00-"
today = driver.find_element('xpath', f"//*[contains(text(), {day})]").find_element('xpath', '..').find_element('xpath', f'//*[contains(text(), "{lecture}" )]').click()
print('Lecture found')

# JUST FUCKING CLICK THE BUTTON KURWA
driver.find_element('xpath', '//*[@id="form_hadir"]').click()