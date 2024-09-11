
from django.urls import path

from .metrics import metrics_view
from .views import register_user, login_user, logout_user

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('metrics/', metrics_view),  # Include accounts URLs
]
