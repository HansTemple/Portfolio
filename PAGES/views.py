from django.shortcuts import render
from django.http import *

# Create your views here.

def index(request):
    response = HttpResponse('')
    response.set_cookie('Cookie', 'This is the new coockie', expires=None)
    information = request.GET.get('information')
    print(information)
    context = {}
    return render(request, 'index.html', context)