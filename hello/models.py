from pyexpat import model
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Application(models.Model):
    applicationname = models.CharField(max_length=50, blank=False, null=True)
    contactemail = models.EmailField(max_length=50, blank=False, null=True)
    description = models.CharField(max_length=400, blank=False, null=True)

    def __str__(self):
        return self.applicationname

class LogMessage(models.Model):
    severityvalue = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    assign = models.ForeignKey(User, blank=False, null=True, on_delete=models.SET_NULL)
    email = models.EmailField(max_length=50, blank=False, null=True)
    subject = models.CharField(max_length=100, blank=False, null=True)
    applicationname = models.ForeignKey(Application, blank=False, null=True, on_delete=models.CASCADE)
    message = models.CharField(max_length=400, blank=False, null=True)
    severity = models.IntegerField(choices=severityvalue, default=5)
    log_date = models.DateTimeField("date logged")

    def __str__(self):
        """Returns a string representation of a message."""
        date = timezone.localtime(self.log_date)
        return f"'{self.message}' logged on {date.strftime('%A, %d %B, %Y at %X')}"
