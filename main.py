from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

browser = webdriver.Chrome()
browser.get('https://monkeytype.com')

timers = ['15', '30', '60', '120']
timer_config = 0 # 0 - 15, 1 - 30, 2 - 60, 4 - 90
time.sleep(1)

browser.find_element(By.XPATH, './/div[@timeconfig="' + timers[timer_config] + '"]').click()

# Uncomment the next line if you want to wait before starting
#input('Press Enter to start typing')

delay = 0.03

try:
    while browser.find_element(By.CLASS_NAME, 'word') != 0:
        curr_word = browser.find_element(By.CSS_SELECTOR, '.word.active')
        letters = []

        for l in curr_word.text:
            letters.append(l)

        letters.append(' ')

        for letter in letters:
            ActionChains(browser).send_keys(letter).perform()
            time.sleep(delay)
except NoSuchElementException as e:
    print('No more "word" elements')

print('Done')
input('Press Enter to exit')

browser.close()
