from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_text_input(driver):
    driver.get('http://uitestingplayground.com/textinput')
    wait = WebDriverWait(driver, 10)
    input_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@class="form-control"]')))
    input_field.send_keys('ITCH')

    button = driver.find_element(By.XPATH, "//*[@class='btn btn-primary']")
    button.click()

    assert "ITCH" in button.text, "test failed"

def test_loading_images(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/loading-images.html')
    wait = WebDriverWait(driver, 10)
    load_all_images = wait.until(EC.presence_of_element_located((By.ID, 'landscape')))

    third_img = driver.find_element(By.ID, 'award')
    third_img_alt = third_img.get_attribute('alt')

    assert third_img_alt == 'award', "test failed"

