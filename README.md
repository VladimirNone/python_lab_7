# FastAPI Glossary Application

## Установка и запуск

1. Клонируйте репозиторий:
  ```bash
  git clone https://github.com/...
  cd fastapi-glossary
  ```
2. Соберите и запустите контейнеры:

```bash
docker-compose up --build
```
3. API будет доступно по адресу:

```bash
http://localhost:8099/docs
```
## Операции
- GET /terms/: Получить список всех терминов.
- GET /terms/{term}: Получить данные о конкретном термине.
- POST /terms/: Добавить новый термин.
- PUT /terms/{term_id}: Обновить существующий термин.
- DELETE /terms/{term_id}: Удалить термин.
## Инструменты
- FastAPI для разработки API.
- SQLite для хранения данных.
- Docker для контейнеризации.