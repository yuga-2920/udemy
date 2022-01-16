from django.contrib import admin
from django.urls import path, include
from .views import hellofunction, HelloWorldClass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', hellofunction),
    path('helloworld2/', HelloWorldClass.as_view()),
    path('helloapp/', include('helloapp.urls'))
]
