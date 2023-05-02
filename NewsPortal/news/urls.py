from django.urls import path
from .views import default, detail


urlpatterns = [
    path('posts/', default, name='Default'),
    path('new/<str:slug>', detail, name='detail'),

]