from django import template
from ..models import MenuItem

register = template.Library()

@register.simple_tag
def get_new_items_of_path(items: list) -> list:
    '''
    Функция реализует шаблонный тег возвращющий списко с исключенным первым элементом
    для поддержки рекурсивного подключения шаблона main_menu.html
    '''
    return items[1:]

@register.inclusion_tag('app/menu/includes/main_menu.html')
def draw_menu(menu: str) -> dict:
    '''
    Фнукция реализует шаблонный тег для отрисовки меню
    :param menu: стрковое значение пути url
    '''
    if menu == 'main_menu':
        menu_items = MenuItem.objects.filter(parent__isnull=True)
        return {
            'menu_items': menu_items,
            'menu': menu,
        }
    items_of_path = menu.split('/')
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    return {
        'menu_items': menu_items,
        'menu': menu,
        'items_of_path': items_of_path,
    }