 
from django.shortcuts import render ,HttpResponse
from blog.models import Blog
# Create your views here.
def home(request):
    return render(request,'index.html')
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request,'bloghome.html', context)
def blogpost(request ,slug):
    return HttpResponse(f"You are viewing {slug}")
def contact(request):
    return render(request,'contact.html')
def search(request):
    return render(request,'search.html')