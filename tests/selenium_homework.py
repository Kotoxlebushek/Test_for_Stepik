from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(i):
    return str(math.log(abs(12*math.sin(int(i)))))


link = " http://SunInJuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    output1 = browser.find_element(By.CSS_SELECTOR, ".nowrap[id='input_value']")
    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(f"{calc(output1.text)}")

    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    button.click()

except Exception as error:
    print(f"При тестировании возникла проблема {error}")

finally:
    time.sleep(30), browser.quit()
