# DjangoMenuTree

DjangoMenuTree - это Django приложение для создания и управления древовидными меню. 
Оно позволяет хранить меню в базе данных, редактировать его через стандартную 
административную панель Django и отображать на любой странице с помощью шаблонного тега.

1. Клонируйте репозиторий на вашем локальном компьютере:

   ```bash
   git clone https://github.com/victoria-gaponova/django_menu_app.git
   
2. Перейдите в каталог проекта:

   ```bash
   cd django_menu_app

3. Создайте и активируйте виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # На Windows используйте venv\Scripts\activate

4. Установите зависимости::

   ```bash
   pip install -r requirements.txt

5. Выполните миграции для создания базы данных:

   ```bash
   python manage.py migrate
   
6. Создайте суперпользователя для доступа к админке:

   ```bash
   python manage.py createsuperuser

7. Запустите сервер разработки Django:

   ```bash
   python manage.py runserver

8. Перейдите в административную панель по адресу http://127.0.0.1:8000/admin/, войдите с учетной записью суперпользователя и добавьте элементы меню в разделе "Menu Items".

9. Теперь вы можете создать страницу, на которой хотите отобразить меню, и использовать кастомный тег {% draw_menu 'main_menu' %} для отображения меню. Замените 'main_menu' на название вашего меню.

## Автор проекта

Этот проект создан и поддерживается Викторией Гапоновой.

Если у вас есть вопросы или предложения по улучшению проекта, свяжитесь со мной по адресу victoria.gaponava@gmail.com.