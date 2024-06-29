# news-site
Новинний сайт на Python з використанням Python

# Запуск
1. Встановлюємо та запускаємо базу данних PostgreSQL
2. Переходимо в файл app/app/settings.py, в змінній SECRET_KEY налаштовуємо секретний ключ, а в DATABASES базу данних PostgreSQL
3. Робимо міграції
<br>``
python3 manage.py makemigrations
``<br>
``
python3 manage.py migrate
``
4. Створюємо супер-користувача
<br>``
python3 manage.py createsuperuser
``
5. Запускаємо сервер
<br>``
python3 manage.py runserver
``