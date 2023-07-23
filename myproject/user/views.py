from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'user/index.html')
def about(request):
    return render(request,'user/about.html')
def contact(request):
    return render(request,'user/contact.html')
def signup(request):
    return render(request,'user/signup.html')
def signin(request):
    return render(request,'user/signin.html')

