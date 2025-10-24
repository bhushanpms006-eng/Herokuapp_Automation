from selenium   import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
driver.find_element(By.XPATH,"//input[@id='username']").send_keys("tomsmith")
driver.find_element(By.XPATH,"//input[@id='password']").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//button[@class='radius']").click()

driver.get("https://the-internet.herokuapp.com/tables")

headers = [header.text for header in driver.find_elements(By.XPATH, "//table[@id='table1']//thead//th")]
rows = driver.find_elements(By.XPATH, "//table[@id='table1']//tbody/tr")
table_data = []
for row in rows:
    # Get all columns for this row
    cols = [col.text for col in row.find_elements(By.XPATH, ".//td")]
    # Pair headers with columns
    row_dict = dict(zip(headers, cols))
    table_data.append(row_dict)
for record in table_data:
    print(record)
time.sleep(3)
