## Дипломный проект автотестов для сайта https://reqres.in/

### Проект совмещает UI и API тесты
* UI + API тесты
    * Регистрация пользователя с получением токена
    * Авторизация пользователя
    * Ошибка авторизации если не был введен пароль
    * Отображение ресурса
    * Пользователь не найден
* API тесты
    * Возвращение запрашиваемого номера страницы
    * Количество пользователей на странице
    * Валидация схемы ответа
    * Проверка доступности нескольких страниц


## Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="resources/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="resources/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="resources/logo/pytest.png"></code>
  <code><img width="5%" title="Selene" src="resources/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="resources/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="resources/logo/Github.png"></code>
  <code><img width="5%" title="Jenkins" src="resources/logo/Jenkins.png"></code>
  <code><img width="5%" title="selenoid" src="resources/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="resources/logo/allure.png"></code>
  <code><img width="5%" title="Telegram" src="resources/logo/telegram.png"></code>
  <code><img width="4%" title="Telegram" src="resources/logo/allure_testops.png"></code>
</p>


## Запуск тестов


## <img width="6%" title="Jenkins" src="resources/logo/Jenkins.png"> Запуск тестов из [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_python_5_project/)
Добавить проект в Jenkins и нажать кнопку "Собрать сейчас".

<p><img src="resources/screenshots/Jenkins.png" alt="Jenkins"/></p>

## <img width="6%" title="Allure" src="resources/logo/allure.png"> Пример [Allure](https://jenkins.autotests.cloud/job/qa_guru_python_5_project/19/allure/) отчетов

<p><img src="resources/screenshots/Allure-report.png" alt="Allure in Jenkins"/></p>

В отчетах Allure для каждого UI-теста прикреплен скриншот, лог, ресурс html-страницы и видео прохождения теста

## <img width="5%" title="Allure" src="resources/logo/allure_testops.png"> Интеграция с [Allure TestOps](https://allure.autotests.cloud/launch/27144) 

<p><img src="resources/screenshots/Allure TestOps.png" alt="Allure in Jenkins"/></p>

## <img width="6%" title="Telegram" src="resources/logo/telegram.png"> Отправка отчета в Telegram

<p><img src="resources/screenshots/Telegram.png" alt="Allure in Jenkins"/></p>

### Пример видео прохождения теста


<p align="center">
  <img title="Video" src="resources/video/Video.gif"/>
</p>
