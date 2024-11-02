import random
import string

from locators import TestLocators


def generate_unique_email():
    return (f"{"".join(random.choices(string.ascii_lowercase, k=10))}"
            f"{random.randint(100, 999)}@{"".join(random.choices(string.ascii_lowercase, k=6))}.ru")


def generate_unique_correct_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=6))


def generate_unique_incorrect_password():
    return "".join(random.choices(string.ascii_letters + string.digits, k=5))


def account_login(driver, email, password):
    driver.find_element(*TestLocators.LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*TestLocators.LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*TestLocators.LOGIN_BUTTON).click()
