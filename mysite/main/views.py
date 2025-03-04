from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList


def home(request):
    return render(request, 'main/home.html', {})


def index(request, id):
    ls = ToDoList.objects.get(id=id)
    return render(request, 'main/list.html', {'ls': ls})


def create(request):
    if request.method == 'POST':
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data['name']
            t = ToDoList(name=n)
            t.save()

        return HttpResponseRedirect(f'/{t.id}')

    else:
        form = CreateNewList()
    return render(request, 'main/create.html', {'form': form})
