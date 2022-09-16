from email.mime import application
from django.urls import path
from django.contrib.auth import views as auth_views

from hello import views

#URLs for whole applicaiton, this could have been split for user registraion and log and and appllications tasks
urlpatterns = [
    path("", views.login_page, name="login"),
    path("home/", views.home, name="home"),
    path("log/", views.log_message, name="log"),
    path("tickets/", views.all_tickets, name="tickets"),
    path("password_change/", views.passwordchange, name="changepassword"),
    path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path("register/", views.register_user, name="register"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password/password_reset_confirm.html"), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password/password_reset_complete.html'), name='password_reset_complete'),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path("applications/", views.log_application, name="applications"),
    path("applicationlist/", views.all_apps, name="applicationlist"),
    path("show_application/<app_id>", views.show_application, name="showapplication"),
    path("show_ticket/<ticket_id>", views.show_ticket, name="showticket"),
    path("search_tickets/", views.search_tickets, name="search_tickets"),
    path("update_ticket/<ticket_id>", views.update_ticket, name="update_ticket"),
    path("update_application/<app_id>", views.update_application, name="update_application"),
    path("delete_ticket/<ticket_id>", views.delete_ticket, name="delete_ticket"),
    path("delete_application/<app_id>", views.delete_application, name="delete_application"),
]
