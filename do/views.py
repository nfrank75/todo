from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from .models import Todo
from .forms import TodoForm


def index(request):
    todo = Todo.objects.all()

    form = TodoForm()

    if request.method=='POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    return render(request, 'do/list.html', {'todo':todo, 'form':form})

def update(request, pk):
    todo =  Todo.objects.get(id=pk)

    form = TodoForm(instance=todo)
    if request.method=='POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
        return redirect('/') 
    
    return render(request, 'do/update.html', {'form':form})


def delete(request, pk):
    todo = Todo.objects.get(id=pk)
    
    if request.method=='POST':
        todo.delete()
        return redirect('/') 
        
    return render(request, 'do/delete.html', {'todo':todo})
