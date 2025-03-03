from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
from .forms import CreateNewList


def home(response):
    return render(response, 'main/home.html', {})


def index(response, id):
    ls = ToDoList.objects.get(id=id)
    return render(response, 'main/list.html', {'ls': ls})


def create(response):
    form = CreateNewList()
    return render(response, 'main/create.html', {'form': form})
