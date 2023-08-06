from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import urllib
from urllib.request import urlopen
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from pynput.keyboard import Key, Controller

options=Options()
options = webdriver.ChromeOptions()
options.add_argument("--log-level=3")
options.add_argument("user-data-dir=C:\\Users\\username\\AppData\\Local\Google\\Chrome Beta\\User Data\\")
options.binary_location = "C:\\Program Files\\Google\\Chrome Beta\\Application\\chrome.exe"
options.add_experimental_option("detach",True)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


driver.get("https://www.instagram.com/")
time.sleep(5)
  
#create
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div').click()
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div[2]/div/button').click()
time.sleep(1)
ext = str(").mp4")



fileloc = str("C:\\Users\\username\\Desktop\\kir\\vid\\1") 



desc = str(fileloc+ext)
keyboard = Controller()
time.sleep(1)
keyboard.type(desc)
time.sleep(2)
keyboard.press(Key.enter)
keyboard.release(Key.enter)
time.sleep(5)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[2]/div').click()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[1]/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[2]').click()
time.sleep(1) 
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(1) 
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(1)

driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[1]').send_keys(("text with hashtag #korea #stupid moon #fk pride"))

time.sleep(1)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[3]/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div/div/div/div[1]/div/div/div[3]/div/div').click()
time.sleep(300)
