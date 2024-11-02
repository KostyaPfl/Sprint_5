import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers
from locators import TestLocators
import urls


class TestLogin:
    @pytest.mark.parametrize('button', [
        TestLocators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_PAGE, TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE])
    def test_login_to_buttons_from_main_page(self, driver, button):
        driver.get(urls.URL_MAIN_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.LOGIN_TO_ACCOUNT_BUTTON_MAIN_PAGE))
        driver.find_element(*button).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_LOGIN_FORM))
        helpers.account_login(driver, data.EMAIL, data.PASSWORD)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_to_button_registration_form(self, driver):
        driver.get(urls.URL_REGISTRATION_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_REGISTRANION_FORM))
        driver.find_element(*TestLocators.LOGIN_BUTTON_REGISTRATION_FORM).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_LOGIN_FORM))
        helpers.account_login(driver, data.EMAIL, data.PASSWORD)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_AN_ORDER_BUTTON).is_displayed()

    def test_login_to_button_recover_password_form(self, driver):
        driver.get(urls.URL_FORGOT_PASSWORD)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_FORGOT_PASSWORD_FORM))
        driver.find_element(*TestLocators.LOGIN_BUTTON_PASSWORD_RECOVERY).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_LOGIN_FORM))
        helpers.account_login(driver, data.EMAIL, data.PASSWORD)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        assert driver.find_element(*TestLocators.PLACE_AN_ORDER_BUTTON).is_displayed()
