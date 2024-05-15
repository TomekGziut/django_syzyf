from django.urls import path
from .views import *

urlpatterns = [
    path('biblioteka/', biblioteka, name='biblioteka'),
    path('process-biblioteka/', process_biblioteka, name='process_biblioteka'),
    path('biblioteka/edit3/', edit3, name='edit3'),
]