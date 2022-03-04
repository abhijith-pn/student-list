from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.AuthLoginView.as_view(), name='login'),
    path('logout/', views.AuthLogoutView.as_view(), name='logout'),
    path('register/', views.AuthRegisterView.as_view(), name='register'),
]
