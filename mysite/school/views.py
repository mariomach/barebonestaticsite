from django.shortcuts import render
from django.http import request, HttpResponse, Http404


courseList = ['Math', 'Science', 'English', 'History', 'Computing Science']


# Create your views here.
def index(request):
    return HttpResponse("hello world")

def course(request):
    context = {
        "courses": courseList,
    }
    return render(request, "course/index.html", context)




