from django.shortcuts import render,HttpResponse
from datetime import datetime
from home.models import Contact

# Create your views here.
def index(request):

    }

    
    return render(request,'index.html',context)
    #return HttpResponse('my name is shrez')

def about(request):
    return render(request,'about.html')
   # return HttpResponse('my name is aboutshrez')

def services(request):
    return render(request,'services.html')
    #return HttpResponse('my name is serviceshrez')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        desc = request.POST.get('desc')


        contact = Contact(name=name, email=email , desc=desc ,date=datetime.today())
        contact.save()

        
    return render(request,'contact.html')


def view(request):
    return render(request,'view.html')

def view1(request):
    return render(request,'view1.html')


def view2(request):
    return render(request,'view2.html')


def view3(request):
    return render(request,'view3.html')


def view4(request):
    return render(request,'view4.html')


def view5(request):
    return render(request,'view5.html')






