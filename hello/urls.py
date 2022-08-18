from django.urls import path

from hello import views
from hello.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="hello/tickets.html",
)

urlpatterns = [
    path("", views.login, name="login"),
    path("home/", views.home, name="home"),
    path("log/", views.log_message, name="log"),
    path("tickets/", home_list_view, name="tickets"),
    path("password_change/", views.passwordchange, name="changepassword"),
]
