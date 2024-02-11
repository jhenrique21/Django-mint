from django.urls import path
from galeria.views import index, imagem
from galeria.models import Fotografia
from . import views


urlpatterns = [
    path('', index, name="index"),
    path('imagem/<int:foto_id>', views.imagem, name="imagem"),

]