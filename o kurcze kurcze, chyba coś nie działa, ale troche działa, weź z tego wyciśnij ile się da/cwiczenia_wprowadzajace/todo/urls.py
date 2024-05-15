from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', todo, name='todo'),
    path('process-todo/', process_todo, name='process_todo'),
    path('todo/edit/', edit, name='edit'),
]