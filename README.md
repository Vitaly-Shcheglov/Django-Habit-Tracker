# Django Habit Tracker

## Описание проекта

Django Habit Tracker — это веб-приложение, созданное для отслеживания привычек пользователей. Приложение позволяет пользователям создавать, редактировать и удалять привычки, а также получать уведомления о выполнении привычек. Проект реализован на Django с использованием Django REST Framework для создания API.
                

## Установка

1. **Клонировать репозиторий**:

   git clone https://github.com/yourusername/habit-tracker.git
   cd habit-tracker

2. **Создайте и активируйте виртуальное окружение**:

   python -m venv venv
   .\venv\Scripts\activate  # Для Windows
   # source venv/bin/activate  # Для macOS/Linux

3. **Установите зависимости**:

   pip install -r requirements.txt

4. **Настройте переменные окружения**: Создайте файл `.env` и добавьте необходимые переменные, например:

   TELEGRAM_BOT_TOKEN=your_telegram_bot_token

5. **Примените миграции**:

   python manage.py migrate

6. **Запустите сервер**:

   python manage.py runserver


## Задачи

### Реализованные требования

- **CORS**: Настроен для подключения фронтенда к API на развернутом сервере.
- **Интеграция с Telegram**: Реализована отправка уведомлений через Telegram.
- **Пагинация**: Реализована пагинация для списка привычек.
- **Переменные окружения**: Используются для хранения конфиденциальной информации.
- **Модели**: Все необходимые модели описаны или переопределены.
- **Эндпоинты**: Реализованы все необходимые эндпоинты для работы с привычками.
- **Валидаторы**: Настроены все необходимые валидаторы.
- **Права доступа**: Описанные права доступа заложены.
- **Celery**: Настроены отложенные задачи через Celery.
- **Тесты**: Проект покрыт тестами как минимум на 80%.
- **Лучшие практики**: Код оформлен в соответствии с лучшими практиками.
- **Список зависимостей**: Все зависимости указаны в `requirements.txt`.
- **Flake8**: Результат проверки Flake8 равен 100% (при исключении миграций).
- **GitHub**: Решение выложено на GitHub.


### Эндпоинты

#### Регистрация

- **POST** `/api/users/` — Регистрация нового пользователя.

#### Авторизация

- **POST** `/api/token/` — Получение JWT токена.
- **POST** `/api/token/refresh/` — Обновление JWT токена.

#### Привычки

- **GET** `/api/habits/user/` — Список привычек текущего пользователя с пагинацией (по 5 привычек на страницу).
- **GET** `/api/habits/public/` — Список публичных привычек.
- **POST** `/api/habits/create/` — Создание новой привычки.
- **PATCH** `/api/habits/<int:pk>/edit/` — Редактирование привычки по ID.
- **DELETE** `/api/habits/<int:pk>/delete/` — Удаление привычки по ID.

#### Уведомления

- **GET** `/api/notifications/` — Получение списка уведомлений текущего пользователя.
- **POST** `/api/notifications/` — Создание нового уведомления.

#### Подписки

- **GET** `/api/subscriptions/` — Получение списка подписок текущего пользователя.
- **POST** `/api/subscriptions/` — Создание новой подписки на привычку.


## Подробнее

Чтобы проверить работу ваших эндпоинтов с помощью Postman, вам нужно выполнить следующие шаги:

## Использование Postman

1. Откройте Postman.
2. Создайте новый запрос:
   - Нажмите на "New" и выберите "Request".
   - Введите имя запроса и выберите коллекцию для сохранения (или создайте новую).
3. Выберите метод (GET, POST, PUT, DELETE) и введите URL.
4. Добавьте тело запроса:
   - Для POST и PUT выберите "Body" и установите тип на "raw" с форматом JSON.
   - Вставьте JSON-данные в текстовое поле.
5. Нажмите "Send" для выполнения запроса и посмотрите на ответ.

### 1. Регистрация пользователя

URL: /api/users/  
Метод: POST

Пример запроса:

curl -X POST http://127.0.0.1:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{
    "email": "newuser@example.com",
    "password": "newpassword",
    "phone": "9876543210",
    "city": "New City"
}'


### 2. Авторизация пользователя (получение токена)

URL: /api/token/  
Метод: POST

Пример запроса:

curl -X POST http://127.0.0.1:8000/api/token/ \
-H "Content-Type: application/json" \
-d '{
    "email": "testuser@example.com",
    "password": "testpassword"
}'


Ответ: Вы получите JSON-ответ с access и refresh токенами.

### 3. Создание привычки

URL: /api/habits/create/  
Метод: POST

Пример запроса:

curl -X POST http://127.0.0.1:8000/api/habits/create/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{
    "location": "Park",
    "time": "10:00:00",
    "action": "Jogging",
    "pleasant_habit": false,
    "frequency": 1,
    "time_to_complete": 60,
    "is_public": true
}'


### 4. Создание уведомления

URL: /api/notifications/  
Метод: POST

Пример запроса:

curl -X POST http://127.0.0.1:8000/api/notifications/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{
    "message": "Your habit is due!"
}'


### 5. Создание подписки

URL: /api/subscriptions/  
Метод: POST

Пример запроса:

curl -X POST http://127.0.0.1:8000/api/subscriptions/ \
-H "Authorization: Bearer <your_access_token>" \
-H "Content-Type: application/json" \
-d '{
    "habit": 1  # Укажите ID привычки, на которую хотите подписаться
}'


### Примечания

- Замените <your_access_token> на фактический access токен, полученный при авторизации.
- Убедитесь, что сервер запущен и доступен по указанному адресу (например, http://127.0.0.1:8000/).
- При использовании Postman, вы можете настроить запросы аналогичным образом, выбрав метод POST, указав URL и добавив заголовки и тело запроса в соответствующих полях.


## Отложенные задачи и интеграция с Telegram

В этом проекте реализованы отложенные задачи с использованием Celery для отправки уведомлений пользователям о выполнении привычек. Интеграция с мессенджером Telegram позволяет отправлять напоминания в личные сообщения пользователям.
С помощью Celery и интеграции с Telegram ваше приложение может отправлять своевременные напоминания пользователям о выполнении привычек, что повышает взаимодействие и эффективность использования приложения.


## Тестирование

Для запуска тестов используйте:

python manage.py test

Для проверки покрытия кода с помощью `coverage`:

coverage run manage.py test
coverage report  # Отчет в консоли
coverage html    # HTML отчет

 ## Оркестрация с помощью Docker
  - Для упрощения развертывания и управления проектом используется Docker и Docker Compose. Это позволяет запускать все необходимые сервисы с помощью одной команды. 
  - Создан файл `docker-compose.yaml`, который описывает все необходимые сервисы для работы приложения:
    - **Бэкенд**: Django приложение.
    - **База данных**: PostgreSQL.
    - **Redis**: Для управления очередями задач.
    - **Celery**: Для обработки фоновых задач.
    - **Celery Beat**: Для планирования периодических задач.

### Установка и настройка
 
 ### Предварительные требования

- Python 3.12 или выше
- Django 5.2 или выше
- Django REST Framework
- PostgreSQL
- Simple JWT
- Celery
- Redis
- Docker
 
 Создайте новые миграции и примените их:
   python manage.py makemigrations
   python manage.py migrate

4. Создайте суперпользователя (по желанию):
   python manage.py createsuperuser

5. Запустите сервер:
   python manage.py runserver

6. Установите и настройте Redis:
- **Для Windows**: Используйте WSL или [Redis для Windows](https://github.com/microsoftarchive/redis/releases).
- **Для Linux**: Установите Redis с помощью пакетного менеджера:

sudo apt-get update
sudo apt-get install redis-server

- **Для macOS**: Установите Redis с помощью Homebrew:
brew install redis

Запустите Redis сервер:
redis-server

7. Настройка API ключей Stripe
Зарегистрируйтесь на [Stripe Dashboard](https://dashboard.stripe.com/register) и получите тестовые API ключи. Сохраните ключи в `settings.py` проекта.


### Запуск проекта

- Выполните последовательно следующие команды:  
    sudo apt update
    sudo apt install git
    git – version
    cd var/www
    git clone git@github.com:Vitaly-Shcheglov/\Django-Habit-Tracker.git
    cd var/www/ \Django-Habit-Tracker/
    docker compose up --build -d

### Перейдите по адресу: http://127.0.0.1:8000
  

### Проверка состояния контейнеров

- Чтобы убедиться, что все контейнеры подняты и работают корректно, выполните команду:
   docker-compose ps
- Вы должны увидеть список запущенных контейнеров с их статусом. Убедитесь, что все состояния указаны как Up.

### Просмотр логов

- Для проверки логов работы приложений можно воспользоваться командой:
   docker-compose logs
- Это поможет вам диагностировать возможные проблемы.

### Проверка работоспособности сервисов

- **Бэкенд**: Доступен по адресу [http://localhost:8000](http://localhost:8000).
- **База данных PostgreSQL**: Доступна на порту 5432.
- **Redis**: Доступен на порту 6379.
- **Celery**: Работает в фоновом режиме для обработки задач.
- **Celery Beat**: Работает для периодического выполнения задач.

### Остановка проекта

Для остановки всех сервисов выполните:
    docker-compose down
 
## Настройка удаленного сервера

  - Установлены необходимые пакеты и зависимости:
       - Python
       - Django
       - Gunicorn
       - Nginx
  - Приложение доступно по IP-адресу сервера или домену.
  - Настроены параметры безопасности:
    - Закрыты ненужные порты.
    - Используются SSH-ключи для доступа.
  - Сервер настроен для автоматической перезагрузки приложения при внесении изменений с использованием Systemd или Supervisor.

### Настройка GitHub Actions Workflow

  - Создан файл YAML для GitHub Actions в директории `.github/workflows`.
  - Workflow запускается при каждом push в репозиторий и включает следующие шаги:
  - Запуск тестов проекта.
  - Деплой проекта на удаленный сервер после успешного прохождения тестов.

### Развертывание проекта на сервере с использованием Docker

  - Написан `Dockerfile` для сборки образа проекта.
  - Настроен GitHub Actions для автоматической сборки Docker-образа и его деплоя на удаленный сервер.


## Установка и настройка

### Предварительные требования

- Python 3.12 или выше
- Django 5.2 или выше
- Django REST Framework
- PostgreSQL
- Simple JWT
- Celery
- Redis

### Установка

1. Клонируйте репозиторий:
   git clone https://github.com/Vitaly-Shcheglov/Django-LMS-project.git

2. Установите зависимости:
   pip install -r requirements.txt


3. Создайте базу данных в PostgreSQL и настройте подключение в `settings.py`

4. Создайте новые миграции и примените их:
   python manage.py makemigrations
   python manage.py migrate

4. Создайте суперпользователя (по желанию):
   python manage.py createsuperuser

5. Запустите сервер:
   python manage.py runserver.

6. Установите и настройте Redis:
- **Для Windows**: Используйте WSL или [Redis для Windows](https://github.com/microsoftarchive/redis/releases).
- **Для Linux**: Установите Redis с помощью пакетного менеджера:

sudo apt-get update
sudo apt-get install redis-server

- **Для macOS**: Установите Redis с помощью Homebrew:
brew install redis

Запустите Redis сервер:
redis-server

7. Настройка API ключей Stripe
Зарегистрируйтесь на [Stripe Dashboard](https://dashboard.stripe.com/register) и получите тестовые API ключи. Сохраните ключи в `settings.py` проекта

8. Настройка переменных окружения
Создайте файл `.env` на сервере и добавьте все необходимые переменные окружения. Пример шаблона `.env`:

DEBUG=False
SECRETKEY=вашсекретныйключ
DATABASEURL=вашURLбазыданных

9. Запуск миграций
python manage.py migrate

10. Запуск сервера
python manage.py runserver 0.0.0.0:8000

11. Запуск Workflow
После внесения изменений в код, просто выполните push в репозиторий, и GitHub Actions автоматически запустит тесты и деплой

11. Настройка перед  запуском CI/CD
Выполните последовательно следующие команды:
  cd ~\.ssh
  ssh -vT git@github.com или ssh -t git@github.com
  ssh -l hallovit 84.201.142.158
  sudo ufw status
  sudo ufw enable
  sudo ufw allow 80/tcp
  sudo ufw allow 443/tcp
  sudo ufw allow 22/tcp

11. Запуск Workflow
После внесения изменений в код, просто выполните push в репозиторий, и GitHub Actions автоматически запустит тесты и деплой


## Лицензия

Этот проект лицензируется в соответствии с лицензией MIT. 


## Контакты

Если у вас есть вопросы или предложения по улучшению проекта, пожалуйста, свяжитесь с автором:

- Имя: Виталий Щеглов
- Email: cgfhnfr4@gmail.com
- GitHub: (https://github.com/Vitaly-Shcheglov)