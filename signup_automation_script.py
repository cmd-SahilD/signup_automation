import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://authorized-partner.vercel.app/")
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)

### Set up your Account

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
otp = input("Enter OTP: ")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@class='disabled:cursor-not-allowed']"))
).send_keys(otp)
wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[normalize-space()='Verify Code']"))
).click()

### Agency Details

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
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()

### Professional Experience

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[@role='combobox']"))
).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter an approximate number.']"))
).send_keys("500")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., Undergraduate admissions to Canada.']"))
).send_keys("Undergraduate admission to Canada")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., 90% ']"))
).send_keys("90")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div//div//div[1]//button[1]"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div//div//div[2]//button[1]"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div//div[3]//button[1]"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div//div[4]//button[1]"))
).click()
wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Next']"))
).click()

### Verification and Preferences

wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Enter your registration number']"))
).send_keys("QA12345")
wait.until(
    EC.presence_of_element_located((By.XPATH, "//button[@role='combobox']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Nepal']"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//body[1]/div[4]/div[4]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[2]/div[1]/button[1]"))
).click()
wait.until(
    EC.presence_of_element_located((By.XPATH, "//input[@placeholder='E.g., ICEF Certified Education Agent']"))
).send_keys("ICEF Certified Education Agent")
first_upload_span = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div[1]//div[1]//div[1]//div[1]//span[1]"))
)
first_upload_span.click()
file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
file_inputs[0].send_keys(r"C:\Users\duwal\Downloads\download.jpg")

second_upload_span = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div//div//div//div//div//div//div[2]//div[1]//div[1]//div[1]//span[1]"))
)
second_upload_span.click()
file_inputs = driver.find_elements(By.XPATH, "//input[@type='file']")
file_inputs[1].send_keys(r"C:\Users\duwal\Downloads\download (1).jpg")

wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Submit']"))
).click()
time.sleep(2)


