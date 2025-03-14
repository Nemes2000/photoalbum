from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.PhotoListView.as_view(), name='photo_list'),
    path('photo/<int:pk>/', views.PhotoDetailView.as_view(), name='photo_detail'),
    path('photo/new/', views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<int:pk>/delete/', views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('register/', views.register, name='register'),
    path('accounts/logout/', LogoutView.as_view(next_page='photo_list'), name='logout'),
]
