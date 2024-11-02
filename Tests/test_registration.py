from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import data
import helpers
from locators import TestLocators
import urls


class TestRegistration:
    def test_registration(self, driver):
        driver.get(urls.URL_REGISTRATION_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_REGISTRANION_FORM))
        name = data.NAME
        email = helpers.generate_unique_email()
        password = helpers.generate_unique_correct_password()
        driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_LOGIN_FORM))
        helpers.account_login(driver, email, password)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PLACE_AN_ORDER_BUTTON))
        driver.find_element(*TestLocators.PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT_EMAIL_FIELD))
        assert driver.find_element(*TestLocators.PERSONAL_ACCOUNT_EMAIL_FIELD).get_attribute('value') == email

    def test_registration_password_error(self, driver):
        driver.get(urls.URL_REGISTRATION_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_REGISTRANION_FORM))
        name = data.NAME
        email = helpers.generate_unique_email()
        password = helpers.generate_unique_incorrect_password()
        driver.find_element(*TestLocators.REGISTRATION_NAME_INPUT).send_keys(name)
        driver.find_element(*TestLocators.REGISTRATION_EMAIL_INPUT).send_keys(email)
        driver.find_element(*TestLocators.REGISTRATION_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*TestLocators.REGISTRATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.REGISTRATION_INCORRECT_PASSWORD_ERROR))
        assert driver.find_element(*TestLocators.REGISTRATION_INCORRECT_PASSWORD_ERROR).is_displayed()
