from django.urls import path, re_path

from . import views

app_name = 'app'

urlpatterns = [
    path('', views.get_main_menu, name='main_menu'),
    re_path(r'^(?P<path>.+)/$', views.get_sub_menu, name='sub_menu'),
]