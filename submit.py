from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import sys
from selenium.webdriver.support import expected_conditions as EC

username='YOUR_USERNAME'
passw='YOUR_PASSWORD'
arg=sys.argv
#prob=input("Enter the problem code : ")
prob=arg[1]
url="https://codeforces.com/problemset/problem/"+prob
print(url)
#file=input("Enter name of file : ")
file=arg[2]
driver = webdriver.Chrome('chromedriver.exe')
driver.minimize_window()
driver.get(url)



#LOGIN PROCESS
href=driver.find_element_by_link_text("Enter")
href.click()

user_box=driver.find_element_by_id('handleOrEmail')
user_box.send_keys(username)
passw_box=driver.find_element_by_id('password')
passw_box.send_keys(passw)
submit_box=driver.find_element_by_class_name('submit')
submit_box.click()

WebDriverWait(driver,10).until(EC.url_to_be(url))

#UPLOAD PROCESS
driver.find_element_by_name("sourceFile").send_keys("YOUR_SOURCE_FILE_DESTINATION"+file)
upload_box=driver.find_element_by_class_name('submit')
upload_box.click()

#LOGOUT PROCESS
href=driver.find_element_by_link_text("Logout")
href.click()

driver.close()
