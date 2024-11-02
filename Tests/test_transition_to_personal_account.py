from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers
from locators import TestLocators
import urls


class TestTransitionToPersonalAccount:
    def test_transition_to_personal_account(self, driver):
        driver.get(urls.URL_LOGIN)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_LOGIN_FORM))
        helpers.account_login(driver, data.EMAIL, data.PASSWORD)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.EXIT_BUTTON))
        assert driver.current_url == urls.URL_PROFILE