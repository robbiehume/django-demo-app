from django.shortcuts import render
from django.http import HttpResponse


def index(response):
    return HttpResponse('<h1>hello world</h1>')


def view1(response):
    return HttpResponse('<h1>view 1!</h1>')
