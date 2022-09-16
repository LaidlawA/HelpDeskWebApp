from multiprocessing import reduction
from django.shortcuts import redirect, render
from django.utils.timezone import datetime
from django.views.generic import ListView
from django.contrib.auth import login
from .forms import NewUserForm
from django.contrib.auth import authenticate
from django.contrib import messages
from hello.forms import LogMessageForm
from hello.models import LogMessage
from hello.models import Application
from hello.forms import ApplicationForm
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

#View to show tickets that have been raised ordered by severity
def all_tickets(request):
	ticket_list = LogMessage.objects.all().order_by('severity')
	return render(request, 'hello/tickets.html', {'ticket_list':ticket_list})

#View to show applications that have been raised ordered by name
def all_apps(request):
	app_list = Application.objects.all().order_by('applicationname')
	return render(request, 'hello/applicationlist.html', {'app_list':app_list})

#View to delete tickets when the button is clicked
def delete_ticket(request, ticket_id):
	delete_ticket = LogMessage.objects.get(pk=ticket_id)
	delete_ticket.delete()
	return redirect('tickets')

#View to delete applications when the button is clicked
def delete_application(request, app_id):
	delete_application = Application.objects.get(pk=app_id)
	delete_application.delete()
	return redirect('applicationlist')

#View to show applications when the details button is clicked
def show_application(request, app_id):
	app = Application.objects.get(pk=app_id)
	return render(request, 'hello/show_application.html', {'app':app})

#View to show tickets when the details button is clicked
def show_ticket(request, ticket_id):
	ticket = LogMessage.objects.get(pk=ticket_id)
	return render(request, 'hello/show_ticket.html', {'ticket':ticket})

#View to update tickets when the update button is clicked and form is filled
def update_ticket(request, ticket_id):
	update_ticket = LogMessage.objects.get(pk=ticket_id)
	form = LogMessageForm(request.POST or None, instance=update_ticket)
	if form.is_valid():
		form.save()
		return redirect('tickets')

	return render(request, 'hello/update_ticket.html', {'update_ticket':update_ticket, 'form':form})

#View to update applications when the update button is clicked and form is filled
def update_application(request, app_id):
	update_application = Application.objects.get(pk=app_id)
	form = ApplicationForm(request.POST or None, instance=update_application)
	if form.is_valid():
		form.save()
		return redirect('applicationlist')

	return render(request, 'hello/update_application.html', {'update_application':update_application, 'form':form})

#View to search for applications and deplay tickest assigned to them
def search_tickets(request):
	if request.method == "POST":
		searched = request.POST.get('searched')
		tickets = LogMessage.objects.filter(applicationname__applicationname__icontains=searched)

		return render(request, 'hello/search_tickets.html', {'searched':searched, 'tickets':tickets})
	else:
		return render(request, 'hello/search_tickets.html', {})

#View to log the tickets raised
def log_message(request):
    form = LogMessageForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("tickets")
        else:
            return render(request, "hello/log_message.html", {"form": form})
    else:
        return render(request, "hello/log_message.html", {"form": form})

#View to log the applications raised
def log_application(request):
    form = ApplicationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("applicationlist")
        else:
            return render(request, "hello/applications.html", {"form": form})
    else:
        return render(request, "hello/applications.html", {"form": form},)

#View to show login page
def login_page(request):
    return redirect("/accounts/login")

#View to show home page
def home(request):
    return render(request, "hello/home.html")

#View to show tickets page
def tickets(request):
    return render(request, "hello/tickets.html")

#View to show applications page
def applications(request):
    return render(request, "hello/applications.html")

#View to show password change page
def passwordchange(request):
    return redirect("/accounts/password_change")

#View to show register page and form
def register_user(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username=username, password=password)
			login(request, user)
			messages.success(request, ("Registration Successful!"))
			return redirect("home")
	else:
		form = NewUserForm()

	return render (request=request, template_name="registration/register.html", context={"register_form":form})

#View to show password reset page and display form/post email repsonse locally
def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000', #works locally only
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/password_reset.html", context={"password_reset_form":password_reset_form})
