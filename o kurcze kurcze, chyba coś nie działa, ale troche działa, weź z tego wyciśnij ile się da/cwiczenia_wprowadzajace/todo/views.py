from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Todo


def todo(request):
  todo = Todo.objects.all().values()
  template = loader.get_template('todo.html')
  context = {
    'todo': todo,
  }
  return HttpResponse(template.render(context, request))

def edit(request):
  return render(request, 'edit.html')


def process_todo(request):
  if request.method == 'POST':
    name = request.POST.get('name')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')

    # Create a new patient entry in the database using the Patient model
    todo = Todo(name=name, start_date=start_date, end_date=end_date)
    todo.save()

    return redirect('todo')  # Redirect back to the todo list view
  else:
    return HttpResponse("Invalid request method.")




