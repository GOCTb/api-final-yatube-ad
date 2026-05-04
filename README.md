# api_final
api final
# API для Yatube

Проект предоставляет REST API для социальной сети Yatube с возможностью создания постов, комментариев, подписок на авторов и управления сообществами. Аутентификация реализована через JWT-токены.

## Установка и запуск

1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение.
3. Установите зависимости: `pip install -r requirements.txt`
4. Выполните миграции: `python manage.py migrate`
5. (Опционально) Загрузите тестовые данные: `python manage.py create_test_data`  
   Пользователи: `regular_user` / `iWannaBeAdmin`, `root` / `5eCretPaSsw0rD`, `second_user` / `iWannaBeAdmin`.  
   Подписки **не** создаются — их можно протестировать через API.
6. Запустите сервер: `python manage.py runserver`

## Примеры запросов

### Получение JWT-токена
POST /api/v1/jwt/create/
{
    "username": "regular_user",
    "password": "iWannaBeAdmin"
}

### Создание поста
POST /api/v1/posts/
Authorization: Bearer <access_token>
{
    "text": "Новый пост",
    "group": 1
}

### Подписка на пользователя
POST /api/v1/follow/
Authorization: Bearer <access_token>
{
    "following": "root"
}

### Список подписок
GET /api/v1/follow/
Authorization: Bearer <access_token>
