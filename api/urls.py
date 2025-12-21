from django.urls import path
from . import views

urlpatterns=[
    path('add/',views.Add_student_view,name='add'),
    path('all/',views.all_student_view,name='all'),
    path('update/<int:pk>/',views.update_view,name='update'),
    path('delete/<int:pk>/',views.Delete_view,name='delete')
]