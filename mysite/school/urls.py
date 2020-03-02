from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("home", views.course, name="home"),
    path("<str:student_id>", views.studentPage, name="studentpages"),
    # path('student', views.studentPage),
    # path("1", views.studentPage),
    # path("<str:student_id>", views.studentPage)
]