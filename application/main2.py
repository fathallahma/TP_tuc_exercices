from selenium import webdriver
import time
import random 
from selenium.webdriver.common.by import By

def return_title():
    driver = webdriver.Chrome()
    driver.get("https://www.hezz2.com/")
    return driver.title
    


