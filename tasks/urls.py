from django.urls import path,include
from tasks.views import manager_dasbord,user_dasbord,test,create_task,view_task,dashbord
urlpatterns = [
    path("manager-dashbord/",manager_dasbord, name="manager-dashbord"),
    path("user-dashbord/",user_dasbord,name="user-dashbord"),
    path("test/",test),
    path("create_task/",create_task),
    path("view_task/",view_task),
    path("dashbord/",dashbord),
    
]
