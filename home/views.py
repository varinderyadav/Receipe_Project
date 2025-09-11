from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home (request):
    peoples = [
        {'name': 'vicky', 'age':'20'},
        {'name': 'sam', 'age':'21'},
        {'name': 'yuvi', 'age':'22'},
        {'name': 'parker', 'age':'15'},
        {'name': 'jack', 'age':'14'},
    
    ]

    vegetables = ['pumpkin','cucumber','brinjle']
    return render(request,"home/index.html", context = {'peoples':peoples,'vegetables':vegetables})

def about (request):
    return render(request,"home/about.html")


def contact (request):
    return render(request,"home/contact.html")

def success_page(request):
    return HttpResponse("hi this is a success page")
