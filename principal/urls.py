
from django.contrib import admin
from django.urls import path, include
from galeria.views import index, imagem

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls')),
    path('imagem/', imagem, name='imagem'),
]
