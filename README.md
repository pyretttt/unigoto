![Tests](https://github.com/pyretttt/unigoto/actions/workflows/python-app.yml/badge.svg)

# unigoto
Итоговый проект по дисциплине проектный практикум

# Сервис для подбора вузов по интересам

## Содержание

[1. Описание приложения](https://github.com/pyretttt/unigoto/blob/main/README.md#Описание-приложения)

[2. ScreenShot диалогов](https://github.com/pyretttt/unigoto/blob/main/README.md#ScreenShot-диалогов)

[3. Запуск приложения](https://github.com/pyretttt/unigoto/blob/main/README.md#Запуск-приложения)

[4. Ссылка на приложение](https://github.com/pyretttt/unigoto/blob/main/README.md#Ссылка-на-приложение) 

[5. Авторы](https://github.com/pyretttt/unigoto/blob/main/README.md#Авторы)

## Описание приложения
   Проект для сервиса UniGoTo. Решение предоставляет пользователю список ВУЗов, которые могли бы быть ему интересны, на основе введенных пользователем анкетных данных. В процессе создания решения проведенно исследование различных подходов к предобработке данных, а также различных моделей для решения данной задачи.
   
   :arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)
   
## Пример работы
![Иллюстрация к проекту](https://github.com/pyretttt/unigoto/blob/main/screenshots/example.jpg)

:arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)

## Запуск сервера FastAPI

`uvicorn src.api.server:app --reload`

При запуске клиента на удаленном сервере, нужно поменять значение переменной `baseUrl` в `src/client/app.js`. Во время разработки удобнее держать это значение в захардкоженном виде, но при деплое стоить брать его из переменной окружения.

## Авторы
* [@Zhenya127](https://github.com/Zhenya127): Евгения Прасолова
* [@pyretttt](https://github.com/pyretttt): Семен Бакулин
* [@Den2909](https://github.com/Den2909): Денис Тряпицын
* [@danil-makushev](https://github.com/danil-makushev): Данил Макушев

:arrow_up:[к содержанию](https://github.com/pyretttt/unigoto/blob/main/README.md#Содержание)