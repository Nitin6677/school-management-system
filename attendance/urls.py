from django.urls import path
from .import views

urlpatterns = [
        path('attend/',views.attendance_view,name="attendance_list"),
]