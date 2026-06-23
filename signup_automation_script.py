import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://authorized-partner.vercel.app/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//button[normalize-space()='Get Started']").click()
wait.until(
    ec.element_to_be_clickable((By.ID, "remember"))
).click()
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()

time.sleep(2)


