from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('imagem/', views.imagem, name="imagem")
]