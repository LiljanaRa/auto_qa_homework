from selenium.webdriver.common.by import By
import time


class TestClass:
    def test_find_logo_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.XPATH, "//*[@class='tn-atom__img t-img loaded']")
        time.sleep(3)
        assert element, 'тест не прошел'

    def test_find_programs_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'Программы')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_payment_methods_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'Способы оплаты')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_news_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'Новости')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_about_us_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'О нас')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_feedback_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'Отзывы')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_button_de_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'de')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_find_button_ru_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.LINK_TEXT, 'ru')
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)

    def test_click_handset_on_page(self, driver):
        driver.get("https://itcareerhub.de/ru")
        element = driver.find_element(By.XPATH, "//*[@class='tn-atom__img t-img loaded']")
        assert element, 'тест не прошел'
        element.click()
        time.sleep(3)


