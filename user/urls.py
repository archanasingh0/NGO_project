from django.urls import path
from . import views

urlpatterns=[
    path('index/',views.index),
    path('home/',views.home),
    path('aboutus/',views.aboutus),
    path('contactus/',views.contactus),
    path('gallery/',views.gallery),
    path('video/',views.video),
    path('blog/',views.blog),
    path('membership/',views.membership),
    path('login/',views.login),
    path('donate/',views.donate),
    path('details/',views.vdodetails),
    path('', views.home),

]