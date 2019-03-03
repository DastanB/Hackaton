from django.urls import path
from auth_ import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/create/', views.ProfileView.as_view(), name='createprofile'),
    path('profile/list/', views.ProfileListView.as_view(), name='listprofile'),
    path('profile/list/<int:pk>/', views.ProfileListView.as_view()),
    
]