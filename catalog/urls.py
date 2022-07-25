from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('films/', views.films_saved, name='films')

]
