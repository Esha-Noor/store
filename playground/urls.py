#map urls to view functions
from django.urls import path
from . import views

#urlconf
urlpatterns=[
    path('hello/', views.say_hello)
]