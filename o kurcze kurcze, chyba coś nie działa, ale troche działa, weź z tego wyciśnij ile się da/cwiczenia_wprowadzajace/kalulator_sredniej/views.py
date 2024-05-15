from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Kalulator_sredniej


def kalulator_sredniej(request):
  kalulator_sredniej = Kalulator_sredniej.objects.all().values()
  template = loader.get_template('kalulator_sredniej.html')
  context = {
    'kalulator_sredniej': kalulator_sredniej,
  }
  return HttpResponse(template.render(context, request))

def edit2(request):
  return render(request, 'edit2.html')

def avg(lista_ocen):
  lista_ocen_float = []
  for i in lista_ocen.split(','):
    lista_ocen_float.append(float(i))
  avg = sum(lista_ocen_float) / len(lista_ocen_float)
  return round(avg, 2)

def process_kalulator_sredniej(request):
  if request.method == 'POST':
    nazwa_przedmiotu = request.POST.get('nazwa_przedmiotu')
    lista_ocen = request.POST.get('lista_ocen')
    średnia_ocen = avg(lista_ocen)

    # Create a new patient entry in the database using the Patient model
    kalulator_sredniej = Kalulator_sredniej(nazwa_przedmiotu=nazwa_przedmiotu, lista_ocen=lista_ocen, średnia_ocen=średnia_ocen)
    kalulator_sredniej.save()

    return redirect('kalulator_sredniej')  # Redirect back to the todo list view
  else:
    return HttpResponse("Invalid request method.")



