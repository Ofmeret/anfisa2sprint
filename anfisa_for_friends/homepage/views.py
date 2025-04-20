# from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    # Запрос:
    # ice_cream_list = IceCream.objects.values(
    #     'id', 'title', 'description'
    #     ).filter(
    #         # Делаем запрос, объединяя два условия
    #         # через Q-объекты и оператор AND:
    #         Q(is_published=True) &
    #         (Q(is_on_main=True) | Q(title__contains='пломбир'))
    #     )
    # Полученный из БД QuerySet передаём в словарь контекста:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    # Словарь контекста передаём в шаблон, рендерим HTML-страницу:
    return render(request, template, context)
