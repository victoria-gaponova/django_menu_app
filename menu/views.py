from django.views.generic import TemplateView


class MenuView(TemplateView):
    """
    Представление для отображения меню.

    Атрибуты класса:
        template_name (str): Имя шаблона для отображения меню.
    """

    template_name = "menu/menu.html"
