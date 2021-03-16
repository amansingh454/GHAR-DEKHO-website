from django.shortcuts import render

# Create your views here.
def listings(request):
    return render(request,'listing/listings.html')
def listing(request,id):
    return render(request,'listing/listing.html')

