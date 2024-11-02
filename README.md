# Sprint_5
## реализованные тесты:
### Файл test_constructor_selection:
1. test_constructor_selection_activ_category - переход в активный по умолчинию раздел конструктора
2. test_constructor_selection_not_activ_category - переход в не активный по умолчинию раздел конструктора
### Файл test_login:
1. test_login_to_buttons_from_main_page - авторизация на сайте при переходе с кнопок "Войти в аккаунт" и "Личный кабинет" на главной странице
2. test_login_to_button_registration_form - авторизация на сайте при переходе с кнопки "Войти" в форме регистрации
3. test_login_to_button_recover_password_form - авторизация на сайте при переходе с кнопки "Войти" в форме восстановления пароля
### Файл test_logout:
1. test_logout_from_account - выход из аккаунта при помощи кнопки "Выход" в личном кабинете
### Файл test_registration:
1. test_registration - успешная регистрация нового пользователя
2. test_registration_password_error - появление ошибки при вводе не валидного пароля в форме регистрации
### Файл test_transition_to_constructor:
1. test_transition_to_constructor_from_personal_account - переход в конструктор из личного кабинета при нажатии на кнопку "Конструктор" и на логотип
### Файл test_transition_to_personal_account:
1. test_transition_to_personal_account - переход в личный кабинет при нажатии на кнопку "Личный кабинет"
## Вспомогательные функции в файле helpers:
1. generate_unique_email - генерация уникального email 
2. generate_unique_correct_password - генерация уникального пароля из 6 символов
3. generate_unique_incorrect_password - генерация уникального пароля из 5 символов
4. account_login - авторизация на сайте