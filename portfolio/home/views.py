from django.shortcuts import render, HttpResponse
from home.models import Contact
# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage(/)")
    context = {'name':'Harry','course':'Django'}
    return render(request, 'home.html',context)

def about(request):
    # return HttpResponse("This is my aboutpage(/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my projects page(/projects)")
    return render(request, 'projects.html')

def contact(request):
    if request.method == "POST":
        Name = request.POST['Name'] 
        email = request.POST['email']
        phone = request.POST['phone']
        # print(Name,email,phone)
        contact = Contact(Name=Name,email=email,phone=phone)
        contact.save()
        print("The data has been save in database.")

    # return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.html')