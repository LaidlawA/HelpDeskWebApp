from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView

from hello.forms import LogMessageForm
from hello.models import LogMessage


class HomeListView(ListView):
    """Renders the home page, with a list of all polls."""

    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("home")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})

def login(request):
    return redirect("/accounts/login")

def home(request):
    return render(request, "hello/home.html")

def passwordchange(request):
    return redirect("/accounts/password_change")
