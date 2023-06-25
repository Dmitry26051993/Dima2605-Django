from django.shortcuts import redirect
from django.http import HttpResponse
import datetime
from django.shortcuts import render

def get_data(request):
    a = datetime.datetime.now()
    return HttpResponse(a)

def two_pow(request, number):
    res = int(number) ** 2
    return HttpResponse(f"res = {res}")
def hello_admin(request):
    return HttpResponse('hello admin')


def hello_guest(request, name):
    return HttpResponse(f'hello {name}')


def hello_user(request, user):
    if user == 'admin':
        return redirect('admin')
    else:
        return redirect('hello_guest', name=user)


def my_word(request, word):
    if len(word) % 2:
        return redirect('get_data')
    else:
        return HttpResponse(f'{word[::2]}')


def login(request):
    if request.method == "POST":
        pass
    else:
        name2 = request.GET.get('name1')
        return redirect('success', name10=name2)

def success(request, name10):
    return HttpResponse("hello" + name10)

def add_user(request):
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        age = request.POST.get('age')
        return HttpResponse(f'name - {name}, lastname - {lastname}, age - {age}')
    else:
        pass

# Create your views here.
