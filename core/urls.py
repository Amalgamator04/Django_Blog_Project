from django.urls import path
from .views import (
    CustomLoginView,
    CustomLogoutView,
    create_post,
    delete_post,
    home,
    profile,
    register,
)

urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:pk>/delete/', delete_post, name='delete_post'),
]
