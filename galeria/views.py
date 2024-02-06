from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "galeria/index.html")
"""
def sauda(request, name):
    return render(request, "pedidos/sauda.html",{
        "name": name.capitalize()
    })"""