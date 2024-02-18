from selenium import webdriver
from time import sleep
dr = webdriver.Chrome()
dr.get("https://www.google.com")
sleep(5)