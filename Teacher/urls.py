from django.urls import path
from .views import teacher_add_view,teacher_all_view,teacher_update_view,teacher_delete_view

urlpatterns =[
    path('techall/',teacher_all_view,name='teachall'),
    path('teacher/',teacher_add_view,name='teacheradd'),
    path('update/<int:pk>/',teacher_update_view,name='update'),
    path('delete/<int:pk>/',teacher_delete_view,name ='delete')

]