from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('home/',views.index),
    path('',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('signin/',views.signin),
    path('signup/',views.signup),
]