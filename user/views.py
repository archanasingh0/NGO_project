from django.shortcuts import render
from .models import *

# Create your views here.

def index(request):
    return render(request,'user/index.html')


def index(request):

    return render(request, 'user/index.html')

def home(request):
    data = slider.objects.all().order_by('-id')[0:4]
    d =iblog.objects.all().order_by('-id')[0:3]
    mydict = {"res": data, "data": d}
    return render(request, 'user/home.html',mydict)
def aboutus(request):
    return render(request,'user/aboutus.html')
def contactus(request):
    status=False
    if request.method=="POST":
        x=request.POST.get('Name')
        y=request.POST.get('Email')
        z=request.POST.get('Mobile')
        a=request.POST.get('msg')
        contact(Name=x,Email=y,Mobile=z,Message=a).save()
        status=True
    return render(request,'user/contactus.html',context={"msg":status})

def gallery(request):
    d=igallery.objects.all().order_by('-id')
    mydict={"data":d}
    return render(request,'user/gallery.html',context=mydict)

def video(request):
    data=vgallery.objects.all().order_by('-id')
    mydict={"vdata":data}
    return render(request,'user/video.html',mydict)

def blog(request):
    x=iblog.objects.all().order_by('-id'),
    mydict = {"bdata":x}
    return render(request,'user/blog.html',mydict)

def membership(request):
    cities=city.objects.all().order_by('-id')
    if request.method == "POST":
        a=request.POST.get('mname')
        b=request.POST.get('mpincode')
        c=request.POST.get('mcity')
        d=request.POST.get('memail')
        e=request.POST.get('mbank')
        f=request.POST.get('mcompany')
        g=request.POST.get('maddress')
        imembership(mname=a,mpincode=b,mcity=c,memail=d,mbank=e,mcompany=f,maddress=g).save()
    mydict={"ct":cities}
    return render(request,'user/membership.html',mydict)

def login(request):
    return render(request, 'user/login.html')
def donate(request):
    countries=icountry.objects.all().order_by('-id')
    states=istate.objects.all().order_by('-id')
    if request.method=="POST":
        am=request.POST.get('damount')
        first=request.POST.get('dfname')
        last=request.POST.get('dlname')
        email=request.POST.get('demail')
        phone=request.POST.get('dphone')
        co=request.POST.get('dcountry')
        address=request.POST.get('dadd')
        sta=request.POST.get('dstate')
        pinc=request.POST.get('dcode')
        occupation=request.POST.get('doccu')
        idonate(damount=am,dfname=first,dlname=last,demail=email,dphone=phone,dcountry=co,dadd=address,dstate=sta,dcode=pinc,doccu=occupation).save()
    mydict = {"dt": countries,"st":states}
    return render(request,"user/donate.html",mydict)

def vdodetails(request):
    y=request.GET.get('msg')
    x=vgallery.objects.all().filter(id=y)
    mydict={"vdata":x}
    return render(request,'user/details.html',mydict)