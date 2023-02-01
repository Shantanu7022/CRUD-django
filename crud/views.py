from django.shortcuts import render

def homepage(request):

   return render(request,'index.html')

def registerpage(request):
    return render(request,'register.html')

def login(request):
    return render(request,'login.html')

# Create your views here.
