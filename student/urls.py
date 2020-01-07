from django.urls import path
from student import views

urlpatterns = [
    path('student/',views.StudentList.as_view()), # API for Student GET or POST request
]

