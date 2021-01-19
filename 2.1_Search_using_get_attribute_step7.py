import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/get_attribute.html'
    browser.get(url)
    x_element = browser.find_element_by_css_selector('#treasure')
    x = x_element.get_attribute('valuex')
    y = calc(x)


    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    submit = browser.find_element_by_class_name('btn')
    submit.click()

finally:
    time.sleep(7)
    browser.quit()