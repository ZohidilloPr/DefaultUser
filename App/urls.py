from django.urls import path
from .views import (Home,
                    SignUp_function,
                    Login_function,
                    LogOut_function,
                    Update_function
                    )
from django.conf import settings
from django.conf.urls.static import static

app_name = 'App'


urlpatterns = [
    path('', Home, name='Home'),
    path('signup', SignUp_function, name='SignUp'),
    path('login', Login_function, name='LogIn'),
    path('logout', LogOut_function, name='LogOut'),
    path('update', Update_function, name='Update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
