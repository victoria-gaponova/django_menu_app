from django import template
from django.utils.safestring import mark_safe
from django.urls import resolve
from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    """
    Выводит меню с указанным именем.

    Аргументы:
        context (dict): Контекст шаблона.
        menu_name (str): Имя меню.

    Возвращает:
        str: HTML-разметка для меню.

    """
    request = context["request"]  # Получаем объект запроса из контекста
    current_url = resolve(request.path_info).url_name  # Получаем текущий URL страницы
    menu = MenuItem.objects.filter(name=menu_name).first()
    if menu:
        return mark_safe(draw_menu_recursive(menu, current_url))
    return ""


def draw_menu_recursive(menu, current_url):
    """
    Рекурсивная функция для генерации HTML-разметки для меню.

    Аргументы:
        menu (MenuItem): Элемент меню.
        current_url (str): Текущий URL страницы.

    Возвращает:
        str: HTML-разметка для меню.

    """
    html = '<li><a href="{}">{}</a>'.format(menu.url, menu.name)
    if menu.children.exists():
        html += "<ul>"
        for item in menu.children.all():
            if item.url == current_url:
                html += '<li class="active">'
                ancestors = item.get_ancestors(ascending=True, include_self=False)
                for ancestor in ancestors:
                    html += "<ul>"
                    html += '<li><a href="{}">{}</a></li>'.format(
                        ancestor.url, ancestor.name
                    )
                    html += "</ul>"
                html += "<ul>"
                for child in item.children.all():
                    html += '<li><a href="{}">{}</a></li>'.format(child.url, child.name)
                html += "</ul>"
                html += "</li>"
            else:
                html += draw_menu_recursive(item, current_url)
        html += "</ul>"
    html += "</li>"
    return html
