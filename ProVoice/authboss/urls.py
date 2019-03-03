from django.urls import path, include
from .views import LoginView, LogoutView, PasswordResetView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
]
