from django.shortcuts import render
import random

import requests
from faker import Faker 
# Create your views here.
def index(request):
    return render(request, 'index.html')

def hello(request):

    username='박지우'

    result={
        'username' : username,
    }
    return render(request, 'hello.html',result)

def lunch(request):
    menus=['라면','삼겹살','치킨']

    pick = random.choice(menus)

    result= {
        'pick':pick,
    }

    return render(request,'lunch.html',result)

def lotto(request):
    numbers=range(1,46)

    pick = random.sample(numbers,6)

    result= {
        'pick':pick,
    }

    return render(request,'lotto.html',result)


def greeting(request, name):
    result = {
        'name': name,
    }

    return render(request, 'greeting.html', result)


def cube(request, num):
    result = {
        'num': num,
        'cube': num ** 3,
    }

    return render(request, 'cube.html', result)


def posts(request):

    fake=Faker()

    fake_posts=[]

    for i in range(100):
        fake_posts.append(fake.text())

    result= {
        'posts': fake_posts,
    }

    return render(request, 'posts.html', result)    
