from django.http import HttpResponse

def index(request):
    return HttpResponse('this is my home page of my site project')