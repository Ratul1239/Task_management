from django.urls import path
from users.views import sing_up, sing_in, sing_out, activate_user

urlpatterns = [
    path('sing-up/', sing_up, name='sing-up'),
    path('sing-in/', sing_in, name='sing-in'),
    path('sing-out/', sing_out, name='sing-out'),
    path('activated/<int:user_id>/<str:token>/', activate_user, name='activate'),  # ✅ ঠিক করা
]
