from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/',include('api.urls')),
    path('auth/',include('auth_app.urls')),
    path('att/',include('attendance.urls')),
    path('tech/',include('Teacher.urls')),
    path('tt/',include('app2.urls')),
    
]
