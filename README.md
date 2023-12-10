![Tests](https://github.com/pyretttt/unigoto/actions/workflows/python-app.yml/badge.svg)

# unigoto

## Запуск сервера FastAPI

`uvicorn src.api.server:app --reload`

При запуске клиента на удаленном сервере, нужно поменять значение переменной `baseUrl` в `src/client/app.js`. Во время разработки удобнее держать это значение в захардкоженном виде, но при деплое стоить брать его из переменной окружения.
