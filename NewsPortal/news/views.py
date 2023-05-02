from django.shortcuts import render
from .models import New


def default(request):
    news = New.objects.all()
    news = New.objects.order_by('-date_pub')
    return render(request, 'default.html', context={'news': news})


def detail(request, slug):
    new = New.objects.get(slug__iexact=slug)
    return render(request, 'detail.html', context={'new': new})

