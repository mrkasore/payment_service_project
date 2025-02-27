Интеграция платежной системы Stripe

ТЕСТОРОВАНИЕ НА СЕРВЕРЕ:

- Для теста перейти по http://109.172.6.59/item/1

- Чтобы протестировать Модель Order перейти по ссылке http://109.172.6.59/items

РАЗВЕРНУТЬ ЛОКАЛЬНО:

1) создать .env файл:

SECRET_KEY=

STRIPE_PUBLIC_KEY=

STRIPE_SECRET_KEY=

YOUR_DOMAIN="http://..."

IP_SITE=

2) Развернуть докер:
- docker-compose up -d или docker compose up -d (если используется Docker CLI плагин)
- docker-compose exec web python manage.py collectstatic
- docker-compose exec web python manage.py makemigrations
- docker-compose exec web python manage.py migrate
- docker-compose down (чтобы остановить сервисы)

