Итоговый проект по дисциплине проектный практикум

# Сервис для подбора вузов по интересам

## Содержание

[1. Описание приложения](https://github.com/pyretttt/unigoto/blob/main/README.md#Описание-приложения)

[2. Начало работы](https://github.com/pyretttt/unigoto/blob/main/README.md#Начало-работы)

[3. Использование](https://github.com/pyretttt/unigoto/blob/main/README.md#Использование) 

[4. Авторы](https://github.com/pyretttt/unigoto/blob/main/README.md#Авторы)

## Описание приложения
   Проект для сервиса UniGoTo. Решение предоставляет пользователю список ВУЗов, которые могли бы быть ему интересны, на основе введенных пользователем анкетных данных. В процессе создания решения проведенно исследование различных подходов к предобработке данных, а также различных моделей для решения данной задачи.

   Приложение использует расстояние Левенштейн для получения результатов.

   В репозитории натроено автоматическое форматирование при помощи black и линтинг.
   
   :arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)
   
## Начало работы

Рекомендуется работать с приложением через продоставленные API и UI.

Запуск сервера FastAPI:

`uvicorn src.api.server:app --reload`

Клиенское приложение доступно по адресу: 

`http://127.0.0.1:8000`

Swagger доступен по адресу: 

`http://127.0.0.1:8000/docs`

При запуске клиента на удаленном сервере нужно поменять значение переменной `baseUrl` в `src/client/app.js`. Во время разработки удобнее держать это значение в захардкоженном виде, но при деплое стоит брать его из переменной окружения.

## Использование
Приложение имеет UI и один API эндоинт. Пользователю предлагается воспользоваться одним из этих способов при работе с моделью.

![Иллюстрация к проекту](https://github.com/pyretttt/unigoto/blob/main/screenshots/example.png)

:arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)

## Авторы
* [@reurairin](https://github.com/reurairin): Данил Макушев – лидер команды, создание веб приложения, создание документации, координация процессов и контроль качества
* [@pyretttt](https://github.com/pyretttt): Семен Бакулин – разработчик, сбор и предобработка данных, создание модели
* [@Den2909](https://github.com/Den2909): Денис Тряпицын – разработчик, сбор и предобработка данных, настройка окружения
* [@Zhenya127](https://github.com/Zhenya127): Евгения Прасолова – аналитик, создание документации, работа с моделью, контроль качества


:arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)