__author__ = 'mbp'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time

#returns the link of the result found.
def getlink(search_string):
    result = []
    # Use webdriver-manager for automatic ChromeDriver management
    service = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=service)
    browser.get('http://www.google.com/ncr')

    # Use modern By locators instead of deprecated find_element_by_* methods
    elem = browser.find_element(By.NAME, 'q')  # Find the search box
    elem.send_keys(search_string + " xls")
    elem.send_keys(Keys.RETURN)

    time.sleep(11)

    for i in range(4):
        # bing x_path = '//*[@id="b_results"]/li[' + str(i+1) +  ']/h2/a'
        x_path = '//*[@id="rso"]/div[2]/div[' + str(i+1) + ']/div/h3/a'
        try:
            elem = browser.find_element(By.XPATH, x_path)
            result.append(elem.get_attribute('href'))
        except NoSuchElementException:
            print('SOMETHING IS wrong')
    time.sleep(1)
    browser.quit()
    return result


with open('xxx.txt', 'r') as fin:
        data = fin.read().splitlines(True)

with open('xxx.txt', 'w') as fout:
        fout.writelines(data[9:])

for s_string in range(0,9):
    x = getlink(data[s_string].strip())
    for i in range(4):
        try:
            fi = open('SearchLinks.txt',mode='a',newline='\n',encoding = 'utf8')
            fi.write(x[i] + '\n')
            fi.close()
        except IndexError:
            print('list index out of range')
