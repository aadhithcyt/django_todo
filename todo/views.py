from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo

def home(request):
    todos = Todo.objects.all()
    return render(request, 'todo/home.html', {'todos': todos})

def add_todo(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        notes = request.POST['notes']
        Todo.objects.create(subject=subject, notes=notes)
        return redirect('home')
    return render(request, 'todo/form.html')

def view_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/view.html', {'todo': todo})

def edit_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('home')
    return render(request, 'todo/form.html', {'todo': todo})

def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('home')


def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo/index.html', {'todos': todos})

def add(request):
    if request.method == 'POST':
        subject = request.POST['subject']
        notes = request.POST['notes']
        Todo.objects.create(subject=subject, notes=notes)
        return redirect('/')
    return render(request, 'todo/add_edit.html')

def edit(request, id):
    todo = get_object_or_404(Todo, id=id)
    if request.method == 'POST':
        todo.subject = request.POST['subject']
        todo.notes = request.POST['notes']
        todo.save()
        return redirect('/')
    return render(request, 'todo/add_edit.html', {'todo': todo})

def delete(request, id):
    todo = get_object_or_404(Todo, id=id)
    todo.delete()
    return redirect('/')

def view(request, id):
    todo = get_object_or_404(Todo, id=id)
    return render(request, 'todo/view.html', {'todo': todo})
