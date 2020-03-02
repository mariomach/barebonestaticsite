from django.shortcuts import render
from django.http import request, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth import authenticate, login, logout

from .models import Student, Course

courseList = ['Math', 'Science', 'English', 'History', 'Computing Science']

# Create your views here.
# def index(request):
#     return HttpResponse("hello world")

def index(request):
    if not request.user.is_authenticated:
        return render(request, "users/login.html", {"message": None})
    context = {
        "user": request.user
    }
    return render(request, "users/user.html", context)

def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None: #success
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else: #Fail
        return render(request, "users/login.html", {"message": "Invalid credentials"})

def logout_view(request):
    logout(request)
    return render(request, "users/login.html", {"message": "Logged out."})

def course(request):
    context = {
        "courses": courseList,
        "students": Student.objects.all(),
        "newcourses": Course.objects.all(),
    }
    return render(request, "course/index.html", context)

def studentPage(request, student_id):
    # student_id = int(request.POST["enrolled"])
    context = {
        "courses": courseList,
        "students": Student.objects.all(),
        "newcourses": Course.objects.all(),
    }
    return render(request, "course/student.html", context)



