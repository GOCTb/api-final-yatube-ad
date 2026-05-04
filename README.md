# api_final
api final
# API для Yatube

Проект предоставляет REST API для социальной сети Yatube с возможностью создания постов, комментариев, подписок на авторов и управления сообществами. Аутентификация реализована через JWT-токены.

## Установка и запуск

1. Клонируйте репозиторий.
2. Создайте и активируйте виртуальное окружение.
3. Установите зависимости: `pip install -r requirements.txt`
4. Выполните миграции: `python manage.py migrate`
5. Запустите сервер: `python manage.py runserver`

## Примеры запросов

### Получение JWT-токена
POST /api/v1/jwt/create/
{
    "username": "anton",
    "password": "password123"
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
    "following": "tolstoy"
}

### Список подписок
GET /api/v1/follow/
Authorization: Bearer <access_token>