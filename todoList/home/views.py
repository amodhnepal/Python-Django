from django.shortcuts import render, HttpResponse
from home.models import Task
# Create your views here.
def home(request):
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Task(tasktitle= title,taskDesc= desc)
        ins.save()
        context = {'success':True}
    return render(request, 'index.html')

def tasks(request):
    return render(request, 'tasks.html')