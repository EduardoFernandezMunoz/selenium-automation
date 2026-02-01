import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")


# --------------------------------------------------------------------
# 1. FRAMES

# Switch to iFrame by its ID
driver.switch_to.frame("courses-iframe")

# Click on the "Courses" link inside the iframe
driver.find_element(By. XPATH, "//a[text()='Courses']").click()

# Wait until the search input is visible
search_input= WebDriverWait(driver,10).until(
    EC.visibility_of_element_located((By. XPATH, "//input[@type='search']")))

# Type "Selenium" into the search input
search_input.send_keys("Selenium")

# Verify that the input contains the text we just typed
search_text = search_input.get_attribute("value")
assert "Selenium" in search_text

driver.switch_to.default_content()      # Exit iFrames

driver.quit()                           # Close the browser and end the session