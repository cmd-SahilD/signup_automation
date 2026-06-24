import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome()
driver.get("https://authorized-partner.vercel.app/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH, "//button[normalize-space()='Get Started']").click()
wait.until(
    EC.element_to_be_clickable((By.ID, "remember"))
).click()
driver.find_element(By.XPATH, "//button[normalize-space()='Continue']").click()
wait.until(
    EC.presence_of_element_located((By.NAME, "firstName"))
).send_keys("Shahil")
wait.until(
    EC.presence_of_element_located((By.NAME, "lastName"))
).send_keys("Duwal")
wait.until(
    EC.presence_of_element_located((By.NAME, "email"))
).send_keys("bot.ai.test.01@gmail.com")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='00-00000000']"))
).send_keys("9866297155")
wait.until(
    EC.presence_of_element_located((By.NAME, "password"))
).send_keys("1234!@#$asdASD")
wait.until(
    EC.presence_of_element_located((By.NAME, "confirmPassword"))
).send_keys("1234!@#$asdASD")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@class='disabled:cursor-not-allowed']"))
).send_keys("966113")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Verify Code']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Agency Name']"))
).send_keys("ABC Agency")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Role in Agency']"))
).send_keys("QA Engineer")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter Your Agency Email Address']"))
).send_keys("qa@test.com")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Agency Website']"))
).send_keys("https://test.com")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[@class='font-satoshi-regular text-translucent']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Nepal']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Next']"))
).click()
time.sleep(2)


