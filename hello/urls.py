from email.mime import application
from django.urls import path
from django.contrib.auth import views as auth_views

from hello import views

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("log/", views.log_message, name="log"),
    path("tickets/", views.all_tickets, name="tickets"),
    path("password_change/", views.passwordchange, name="changepassword"),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("register/", views.register_request, name="register"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("applications/", views.log_application, name="applications")
]
