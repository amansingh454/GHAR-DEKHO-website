from django.shortcuts import render

def home(request):
    return render(request,'page/home.html')
def about(request):
    return render(request,'page/about.html')
def register(request):
    return render(request,'page/register.html')
def login(request):
    return render(request,'page/login.html')
