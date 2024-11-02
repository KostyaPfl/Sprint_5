import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import TestLocators
import urls


class TestConstructorSelection:
    def test_constructor_selection_activ_category(self, driver):
        driver.get(urls.URL_MAIN_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_CONSTRUCTOR))
        driver.find_element(*TestLocators.SAUCES_SPAN).click()
        driver.find_element(*TestLocators.BUNS_SPAN).click()
        assert 'current' in driver.find_element(*TestLocators.BUNS_SPAN).get_attribute('class')


    @pytest.mark.parametrize('button', [TestLocators.SAUCES_SPAN, TestLocators.FILLINGS_SPAN])
    def test_constructor_selection_not_activ_category(self, driver, button):
        driver.get(urls.URL_MAIN_PAGE)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(TestLocators.HEADING_CONSTRUCTOR))
        driver.find_element(*button).click()
        assert 'current' in driver.find_element(*button).get_attribute('class')
