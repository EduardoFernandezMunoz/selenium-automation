import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# --------------------------------------------------------------------
# 1. BUTTON SELECTION

# Find the radio button with value 'radio3' and click it
radio3 = driver.find_element(By.XPATH, "//input[@value='radio3']")
radio3.click()

# Verify that the radio button is selected
assert radio3.is_selected()


# --------------------------------------------------------------------
# 2. AUTOCOMPLETE: SELECT A COUNTRY

# Enter partial text in the autocomplete input
driver.find_element(By.ID, "autocomplete").send_keys("Ar")

# Get all the names of the countries that appear in the dropdown list
countries = driver.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li")

# Iterate over each option to find the country we are looking for
for country in countries:

    # Get the text of the option
    countryName = country.text

    # Select the option when it is the country we are looking for
    if countryName == "Hungary":
        country.click()
        break #Exit the loop once the correct country is selected


# --------------------------------------------------------------------
# 3. STATIC DROPDOWN

# Locate the dropdown element
dropdown = Select(driver.find_element(By.ID, "dropdown-class-example"))

# Select option by visible text
dropdown.select_by_visible_text("Option1")

# Pause added to make the dropdown change visible
time.sleep(1)

# Select option by index
dropdown.select_by_index(2)

# Verify Option2 is the last option selected (using strip to avoid issues with spaces)
assert dropdown.first_selected_option.text.strip() == "Option2"


# --------------------------------------------------------------------
# 4. CHECKBOXES

# Locate all checkbox elements on the page
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")

# Iterate through each checkbox
for checkbox in checkboxes:

    # Check the value attribute to find the desired checkbox
    if checkbox.get_attribute("value") == "option3":
        checkbox.click()
        assert checkbox.is_selected()               # Verify the checkbox is selected
        break
time.sleep(1)           # Pause added to make the checkbox selection visible


driver.quit()               # Close the browser and end the session