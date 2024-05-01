from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('post/', views.post_dweet, name='post_dweet'),
    path('profile/', views.profile, name='profile'),

    # ... other URL patterns
]