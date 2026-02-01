from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()


driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
driver.implicitly_wait(5)

# --------------------------------------------------------------------
# 1. NAVIGATE TO SHOP PAGE

driver.find_element(By.LINK_TEXT, "Shop").click()


# --------------------------------------------------------------------
# 2. SELECT A SPECIFIC PRODUCT FROM THE SHOP

# Get all product cards displayed on the shop page
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

# Iterate through each product to find the desired one
for product in products:
    product_name = product.find_element(By.XPATH, "div/h4/a").text

    # Add the product to the cart when the name matches
    if product_name == "Samsung Note 8":
        product.find_element(By.XPATH, "div/button").click()


# --------------------------------------------------------------------
# 3. PROCEED TO CHECKOUT

# Click on the checkout button (cart)
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()

# Click on the final checkout button
driver.find_element(By.CSS_SELECTOR, "button[class*='btn-success']").click()

# --------------------------------------------------------------------
# 4. COMPLETE THE PURCHASE FORM

# Type the first letters of the country to trigger the autocomplete
driver.find_element(By. ID, "country").send_keys("Ge")

# Wait until the country suggestion appears and select it
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Germany")))
driver.find_element(By.LINK_TEXT, "Germany").click()

# Accept terms and conditions and submit the form
driver.find_element(By. CSS_SELECTOR,"div[class='checkbox checkbox-primary']").click()
driver.find_element(By. CSS_SELECTOR, "input[type='submit']").click()

# --------------------------------------------------------------------
# 5. VERIFY SUCCESS MESSAGE
success_text = driver.find_element(By. CSS_SELECTOR, "div[class*='alert']").text
assert "Success" in success_text, "Purchase was not successful"


driver.quit()
