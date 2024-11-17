 
from django.shortcuts import render ,HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("This is home")
def blog(request):
    return HttpResponse("this is blog")
def blogpost(request ,slug):
    return HttpResponse(f"You are viewing {slug}")
def contact(request):
    return HttpResponse("This is contact")