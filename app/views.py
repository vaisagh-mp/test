from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .models import *


# Create your views here.
@login_required(login_url='Login')
def home(request):
    results = Product.objects.all()
    return render(request, "home.html", {"Product": results})


def index(request):

    if request.method == 'POST':
        message = request.POST['message']
        send_mail('contact form',
        message,
        settings.EMAIL_HOST_USER,
        ['vaisaghmp@gmail.com'],
    )
    return render(request, 'email.html')
