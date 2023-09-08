from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path("villagerbreader-tutorial/", views.villagebreader, name= "villagebreader"),
]
