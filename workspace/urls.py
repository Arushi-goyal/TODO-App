from .import views
from django.urls import path

urlpatterns = [

    path("", views.index, name='index'),
    path("", views.index2, name='index2')

]
