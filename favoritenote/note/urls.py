from django.urls import path, include
from . import views


urlpatterns = [path('', views.index_note, name='home_note'),
               ]
