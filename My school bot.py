from selenium import webdriver
import time
import pyautogui




driver = webdriver.Chrome('https://cdn.jsdelivr.net/gh/c0der69/MyFiles@main/driver.exe')
driver.maximize_window()
driver.get('https://ssoa.testpedia.in/')

user_input = driver.find_element_by_id('UserName')

user_input.send_keys("1593-2475")

password_input = driver.find_element_by_id('Password')



password_input.send_keys("ca1241 ")

signin_button = driver.find_element_by_id("LoginButton")

signin_button.click()



notification_button = driver.find_element_by_link_text("Notification")

notification_button.click()

plus_button = driver.find_element_by_css_selector(".mdi-plus-box")

plus_button.click()

time.sleep(1)

view_button = driver.find_element_by_partial_link_text('Link')

view_button.click()

time.sleep(1)

link_text = driver.find_element_by_partial_link_text('zoom.us')

link_text.click()


pyautogui.moveTo( 1050,280) 
time.sleep(1)
pyautogui.click()
pyautogui.click()


