from django.urls import path 
from .views import hajeri_view
urlpatterns =[
    path('hajeri/',hajeri_view,name='Hajeri'),
]