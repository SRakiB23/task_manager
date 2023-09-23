from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def home(request):

    clientList = [
        {

            'id': '1',
            'name': 'Sazzad Bashar',
            'profession': 'Web Developer',
        },

        {

            'id': '2',
            'name': 'Hasan Mahmud',
            'profession': 'Police',
        },
    ]

    context = {'client': clientList}

    return render(request, 'index.html', context=context)

def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my_login.html')

