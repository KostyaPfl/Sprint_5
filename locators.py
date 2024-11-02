from selenium.webdriver.common.by import By

class TestLocators:
    #Форма регистрации
    HEADING_REGISTRANION_FORM = [By.XPATH, '//h2[text()="Регистрация"]'] #заголовок формы регистрации
    REGISTRATION_NAME_INPUT = [By.XPATH, '//label[text()="Имя"]/following-sibling::input'] #поле ввода имени в форме регистрации
    REGISTRATION_EMAIL_INPUT = [By.XPATH, '//label[text()="Email"]/following-sibling::input'] #поле ввода email в форме регистрации
    REGISTRATION_PASSWORD_INPUT = [By.XPATH, '//label[text()="Пароль"]/following-sibling::input']  # поле ввода пароля в форме регистрации
    REGISTRATION_BUTTON = [By.XPATH, '//button[text()="Зарегистрироваться"]'] #кнопка "зарегистрироваться" в форме регистрации
    REGISTRATION_INCORRECT_PASSWORD_ERROR = [By.XPATH, "//p[text()='Некорректный пароль']"] #ошибка при некорректном пароле в форме регистрации


    #Переход на форму авторизации
    LOGIN_TO_ACCOUNT_BUTTON_MAIN_PAGE = [By.XPATH, '//button[text()="Войти в аккаунт"]'] #кнопка "Войти в аккаунт" на главной странице
    PERSONAL_ACCOUNT_BUTTON_MAIN_PAGE = [By.XPATH, '//p[text()="Личный Кабинет"]'] #кнопка "Личный кабинет" на главной странице
    LOGIN_BUTTON_REGISTRATION_FORM = [By.XPATH, '//a[text()="Войти"]'] #кнопка войти в форме регистрации
    LOGIN_BUTTON_PASSWORD_RECOVERY = [By.XPATH, '//a[text()="Войти"]']  # кнопка войти в форме восстановления пароля

    #Форма авторизации
    HEADING_LOGIN_FORM = [By.XPATH, '//h2[text()="Вход"]']  # заголовок формы авторизации
    LOGIN_EMAIL_INPUT = [By.XPATH, '//input[@type="text"]']  # поле ввода email в форме авторизации
    LOGIN_PASSWORD_INPUT = [By.XPATH, '//input[@type="password"]']  # поле ввода пароля в форме авторизации
    LOGIN_BUTTON = [By.XPATH, '//button[text()="Войти"]']  # кнопка "Войти" в форме авторизации

    HEADING_FORGOT_PASSWORD_FORM = [By.XPATH, '//h2[text()="Восстановление пароля"]']  # заголовок формы восстановления пароля

    #личный кабинет
    PERSONAL_ACCOUNT_EMAIL_FIELD = [By.XPATH, '//label[text()="Логин"]/following-sibling::input']  # поле "Логин" в личном кабинете
    EXIT_BUTTON = [By.XPATH, '//button[text()="Выход"]']  # кнопка "Выход" в личном кабинете

    #главная страница
    PLACE_AN_ORDER_BUTTON = [By.XPATH, '//button[text()="Оформить заказ"]']  # кнопка "Оформить заказ" на главной странице
    CONSTRUCTOR_BUTTON = [By.XPATH, '//p[text()="Конструктор"]']  #кнопка "конструктор"
    HEADING_CONSTRUCTOR = [By.XPATH, '//h1[text()="Соберите бургер"]']  #заголовок конструктора
    LOGO = [By.XPATH, '//a[@href="/"]'] #логотип "stellarburgers"
    SAUCES_SPAN = [By.XPATH, "//span[text()='Соусы']/parent::div"] #кнопка "Соусы" в конструкторе
    FILLINGS_SPAN = [By.XPATH, "//span[text()='Начинки']/parent::div"] #кнопка "Начинки" в конструкторе
    BUNS_SPAN = [By.XPATH, "//span[text()='Булки']/parent::div"] #кнопка "Булки" в конструкторе (активна по умолчанию)
