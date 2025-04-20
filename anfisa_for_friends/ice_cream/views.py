'''Представления для отображения деталей мороженого и списка мороженого.'''
from django.shortcuts import get_object_or_404, render
from django.db.models import Prefetch

from ice_cream.models import IceCream, Topping


def ice_cream_detail(request, pk):
    '''Функция делает запрос информации к конкретному мороженному'''
    template = 'ice_cream/detail.html'
    ice_cream = get_object_or_404(
        IceCream.objects.select_related('category', 'wrapper').only(
            'title',
            'price',
            'description',
            'category__title',
            'wrapper__title'
        ).prefetch_related(
            Prefetch('toppings', queryset=Topping.objects.only('title'))
        ).filter(is_published=True, category__is_published=True), pk=pk
    )
    return render(request, template, {'ice_cream': ice_cream})


def ice_cream_list(request):
    '''Функция  запроса для страницы Каталог мороженного'''
    template = 'ice_cream/list.html'
    ice_cream_list = IceCream.objects.select_related('category').filter(
        is_published=True,
        category__is_published=True
    ).order_by('category')
    context = {'ice_cream_list': ice_cream_list}
    return render(request, template, context)
