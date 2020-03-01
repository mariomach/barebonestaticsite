from django.urls import path
from . import views

urlpatterns = [
    path("", views.index),
    path("index", views.course),
    # path("<student_id>", views.studentPage)

]