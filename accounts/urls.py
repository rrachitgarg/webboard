from django.contrib import admin
from django.urls import path,include
from .views import signup_view
from django.contrib.auth import views

urlpatterns = [
    path('signup/',signup_view,name='signup'),
    path('logout/',views.LogoutView.as_view(),name="logout"),
    path('login/',views.LoginView.as_view(template_name='login.html'),name='login'),
    path('settings/password/',views.PasswordChangeView.as_view(template_name='password_change.html'),name='password_change'),
    path('settings/password/done/',views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),name='password_change_done'),    
]

