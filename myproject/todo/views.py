from django.shortcuts import render,redirect

# Create your views here.
from .models import Todo
from .forms import TodoForm

def index(request):

	todo_list = Todo.objects.order_by('id')

	form = TodoForm()

	context={'todo_list':todo_list,'form':form}

	return render(request,'todo/index.html',context)

def addTodo(request):
	form = TodoForm(request.POST)
	new_Todo = Todo(text=request.POST['text'])
	new_Todo.save()
	return redirect('index')


def addDone(request,todo_id):
	todo=Todo.objects.get(pk=todo_id)
	todo.complete=True
	todo.save()

	return redirect('index')

def delDone(request):
	Todo.objects.filter(complete__exact=True).delete()

	return redirect('index')

def delAll(request):
	Todo.objects.all().delete()
	return redirect('index')