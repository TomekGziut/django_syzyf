from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Biblioteka


def biblioteka(request):
  bibliotka = Biblioteka.objects.all().values()
  template = loader.get_template('biblioteka.html')
  context = {
    'biblioteka': bibliotka,
  }
  return HttpResponse(template.render(context, request))

def edit3(request):
  return render(request, 'edit3.html')

def process_biblioteka(request):
  if request.method == 'POST':
    book_name = request.POST.get('book_name')

    # Create a new patient entry in the database using the Patient model
    biblioteka = Biblioteka(book_name=book_name)
    biblioteka.save()

    return redirect('biblioteka')  # Redirect back to the todo list view
  else:
    return HttpResponse("Invalid request method.")




