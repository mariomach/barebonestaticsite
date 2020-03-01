from django.shortcuts import render
from django.http import request, HttpResponse, Http404

from .models import Student, Course

courseList = ['Math', 'Science', 'English', 'History', 'Computing Science']


# Create your views here.
def index(request):
    return HttpResponse("hello world")

def course(request):
    context = {
        "courses": courseList,
        "students": Student.objects.all(),
        "newcourses": Course.objects.all(),
    }
    return render(request, "course/index.html", context)


# def studentPage(request):
#     student_id = int(request.POST["enrolled"])
#     context = {
#         "courses": courseList,
#         "students": Student.objects.all(),
#         "newcourses": Course.objects.all(),
#     }
#     return render(request, "course/student.html", context)



