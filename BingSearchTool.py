from userInformation import userDict
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def main():
    for account in userDict.Keys():
        login(account, userDict[account])


def login(accountName, pw):
    driver.get('http://www.google.com')


chromedriver = '‪C:\Python34\Scripts\chromedriver.exe'
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get("http://stackoverflow.com")
driver.quit()
"""
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
"""
driver.close()


#if __name__ == '__main__':
#	main()