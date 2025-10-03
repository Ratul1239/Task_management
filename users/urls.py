from django.urls import path
from users.views import sing_up,sing_in,sing_out
urlpatterns = [
    path('sing-up/',sing_up,name='sing-up'),
    path('sing-in/',sing_in,name='sing-in'),
    path('sing-out/',sing_out,name='sing-out')
]
