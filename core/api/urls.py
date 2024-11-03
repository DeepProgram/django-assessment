from django.urls import path
from .views import RegisterUserView, StatusView

urlpatterns = [
    path('user/', RegisterUserView.as_view(), name="user_registration"),
    path('user/status/', StatusView.as_view(), name="user_status")
]