from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox()
time.sleep(15)
driver.get("http://www.discord.com/login")
time.sleep(30)
driver.find_element_by_name("email").send_keys("email here")
driver.find_element_by_name("password").send_keys("password here")
driver.find_element_by_xpath("//button[@type='submit']").click()
#Now goto desired channel manually
print("Now goto desired channel manually")
time.sleep(30)
msg = driver.find_element_by_xpath("//div[@aria-label='Message #genereal']")
a = 1
while a==1:
  msg.send_keys("Pls beg")
  msg.send_keys(Keys.ENTER)
  time.sleep(30)
  msg.send_keys("Pls dep max")
  msg.send_keys(Keys.ENTER)
  time.sleep(11)

print("Script is no working, no need to print")