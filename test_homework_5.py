from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


def test_text_in_iframe(driver):
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/iframes.html')
    wait = WebDriverWait(driver, 5)
    iframe = wait.until(EC.presence_of_element_located((By.ID, 'my-iframe')))
    driver.switch_to.frame(iframe)
    items = driver.find_elements(By.CLASS_NAME, 'lead')
    assert items
    expected_text = 'semper posuere integer et senectus justo curabitur.'
    count = 0
    for i in items:
        if expected_text in i.text:
            count += 1
    assert count


def test_drag_and_drop(driver):
    driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
    wait = WebDriverWait(driver, 10)
    accept_cookies_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[.="Einwilligen"]')))
    accept_cookies_button.click()

    iframe = driver.find_element(By.XPATH, "//*[@class='demo-frame lazyloaded']")
    driver.switch_to.frame(iframe)

    source = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'ui-widget-content')))
    target = driver.find_element(By.ID, 'trash')

    action = ActionChains(driver)
    action.drag_and_drop(source, target).perform()

    gallery = driver.find_element(By.ID, "gallery")
    count_of_photos_in_gallery = gallery.find_elements(By.TAG_NAME, "li")

    assert len(count_of_photos_in_gallery) == 3, "The number of photos doesn't match"

    trash = driver.find_element(By.ID, 'trash')
    count_of_photos_in_trash = trash.find_elements(By.TAG_NAME, "li")
    assert len(count_of_photos_in_trash) == 1, "The number of photos doesn't match"