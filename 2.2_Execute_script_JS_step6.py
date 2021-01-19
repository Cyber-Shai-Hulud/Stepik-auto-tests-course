import math
from selenium import webdriver
import time


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    url = 'http://suninjuly.github.io/execute_script.html'
    browser.get(url)
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    # people_radio = browser.find_element_by_id("robotsRule")
    # people_checked = people_radio.get_attribute("checked")
    # print("value of people radio: ", people_checked)
    # assert people_checked == "true", "People radio is not selected by default"

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    button = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    radiobutton = browser.find_element_by_css_selector('#robotsRule')
    radiobutton.click()

    button.click()

finally:
    time.sleep(7)
    browser.quit()
