from django.shortcuts import render
from django.http import HttpResponse

data={
    'title': 'Головна сторінка',
    'values' : ['some', 'hello', '123'],
    'obj': {
        'car' : 'BMW',
        'age' : 18,
        'hobby': 'Football'
    }
}

def index(request):
    return render(request, 'main/index.html', data)

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return HttpResponse("<h4>test contacts</h4>")

