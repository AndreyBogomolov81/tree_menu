from django.conf import settings

from .models import MenuItem

def get_url_for_item(object: MenuItem) -> str:
    '''
    Функция для формирования url добавляемого элемента меню
    :param object:
    :return: url включая схему протокола HTTP, IP - адрес, путь запроса
    '''
    if object.parent:
        return '/'.join([object.parent.url, object.slug])

    return '/'.join(
        ['http:/', f'{settings.ALLOWED_HOSTS[0]}:8000', 'main_menu', object.slug]
    )