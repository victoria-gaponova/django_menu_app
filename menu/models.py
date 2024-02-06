from django.db import models

NULLABLE = {"null": True, "blank": True}


class MenuItem(models.Model):
    """
       Модель MenuItem представляет собой элемент меню с древовидной структурой.

       Поля модели:
       - name (CharField): Название элемента меню.
       - parent (ForeignKey): Ссылка на родительский элемент меню. Может быть NULL,
         что означает, что элемент находится на верхнем уровне.
       - url (URLField): URL-адрес, который будет использоваться при клике на элемент
         меню.

        Методы модели:
    - __str__: Возвращает строковое представление объекта
    """

    name = models.CharField(max_length=200)
    parent = models.ForeignKey(
        "self", **NULLABLE, on_delete=models.CASCADE, related_name="children"
    )
    url = models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.name
