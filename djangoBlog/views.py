from django.shortcuts import render
from django.shortcuts import HttpResponse

def home(request):
    return render(request,'home.html')
    # return HttpResponse("Home")
def about(request):
    return render(request,'about.html')
    # return HttpResponse("we are in about, hello world!")
