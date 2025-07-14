from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import ReaderRegisterView, ReaderLoginView, ReaderLogoutView, EditProfileView, DeleteProfileView

urlpatterns = [
    path('register/', ReaderRegisterView.as_view(), name='register'),
    path('login/', ReaderLoginView.as_view(), name='login'),
    path('logout/', ReaderLogoutView.as_view(), name='logout'),
    path('edit/', EditProfileView.as_view(), name='edit_profile'),
    path('delete/', DeleteProfileView.as_view(), name='delete_profile'),
]
