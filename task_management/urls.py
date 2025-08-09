from django.contrib import admin
from django.urls import path,include
from tasks.views import home,contact,resturent

urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",home),
    path("contact/", contact),
    path("resturent/", resturent),    
    path("tasks/", include('tasks.urls'))    

]