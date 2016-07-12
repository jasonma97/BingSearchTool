import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\Users\WenJian\AppData\Local\Google\Chrome\User Data")
driver = webdriver.Chrome(executable_path = "C:\Python34\Scripts\chromedriver.exe")  # Optional argument, if not specified will search path.
driver.get("http://www.bing.com/xhtml")
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
string = '4 Cookies'
for a0 in range(10):
    search_box = driver.find_element_by_name('q')
    search_box.send_keys(string)
    search_box.submit()
    string += a0
driver.quit()