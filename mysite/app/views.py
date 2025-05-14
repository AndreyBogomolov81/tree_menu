from django.http import HttpResponse, Http404
from django.shortcuts import render

from .models import MenuItem

# Create your views here.
def get_main_menu(request):
    '''
    Функция-представление для отображения главного меню с нераскрытыми субэлементами
    '''
    return render(
        request,
        'app/menu/index.html',
        {
            'menu': 'main_menu',
        },
    )


def get_sub_menu(request, path):
    '''
    Функция-представление для отображения выбранного меню
    :param request:
    :param path: часть пути url после неизменной части пути url (main_menu/)
    '''

    # проверка наличия элемента меню по динамической части пути url
    if not  MenuItem.objects.filter(url__contains=path).exists():
        raise Http404

    return render(
        request,
        'app/menu/index.html',
        {
            'menu': path,
        },
    )

