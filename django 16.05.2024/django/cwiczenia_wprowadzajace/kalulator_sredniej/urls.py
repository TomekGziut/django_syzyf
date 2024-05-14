from django.urls import path
from .views import *

urlpatterns = [
    path('kalulator_sredniej/', kalulator_sredniej, name='kalulator_sredniej'),
    path('process-kalulator_sredniej/', process_kalulator_sredniej, name='process_kalulator_sredniej'),
    path('kalulator_sredniej/edit2/', edit2, name='edit2'),
]