from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as p

from selenium import webdriver



driver = webdriver.Chrome()

# Navigate to the login page
driver.get('https://github.com/login')

# Wait for the username field to be present and visible
username_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'login_field'))
)

# Fill in the username field
username_field.send_keys('')

# Wait for the password field to be present and visible
password_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'password'))
)

# Fill in the password field
password_field.send_keys('')

# Wait for the login button to be present and clickable
login_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'btn.btn-primary.btn-block.js-sign-in-button'))
)

# Click the login button
login_button.click()


# Wait for the username field to be present and visible
create_init_repository = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.CLASS_NAME, 'btn.btn-sm.btn-primary'))
)

# Click the Lesson Evaluate
create_init_repository.click()

    # Wait for the repository name field to be present and visible
repository_name_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'repository_name'))
)

# Fill in the repository name field
repository_name_field.send_keys('teste-automation')

        # Wait for the repository name field to be present and visible
repository_description_field = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'repository_description'))
)

# Fill in the repository name field
repository_description_field.send_keys('This is fake, dont trust in this robot')

# Check the readme file
readme_file = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, 'repository_auto_init'))
)

readme_file.click()

p.click(553,778)

input('press enter to end')
driver.close()

