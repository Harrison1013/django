from django.urls import path
from stocks import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get', views.get, name='get'),
]
