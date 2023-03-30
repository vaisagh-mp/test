from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
# from .forms import RegistrationForm
from django.contrib.auth.models import User
from .models import *
# from django.core.mail import send_mail
from django.views.decorators.cache import cache_control


# Verification Email:
# from django.contrib.sites.shortcuts import get_current_site
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
# from django.utils.encoding import force_bytes
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import EmailMessage

from django.contrib.auth import get_user_model
User = get_user_model()

# @login_required(login_url='Login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('First')
        last_name = request.POST.get('Last')
        email = request.POST.get('Email')
        phonenumber = request.POST.get('Phone')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm')
        username = email.split("@")[0]

        if password != confirm_password:
            return HttpResponse("Password and confirm password are not match")
        else:
            my_user = User.objects.create_user(
                first_name=first_name, last_name=last_name, email=email, password=password, username=username)
            my_user.Phone = phonenumber
            my_user.is_active = True
            my_user.save()

            # USER_AUTHENTICATION
            # current_site = get_current_site(request)
            # email_subject = 'Please active your account.'
            # message = render_to_string('acounts/account_verification_email.html', {
            #     'user': my_user,
            #     'domain': current_site,
            #     'uid': urlsafe_base64_encode(force_bytes(my_user.pk)),
            #     'token': default_token_generator.make_token(my_user),
            # })
            # to_email = email
            # send_email = EmailMessage(email_subject, message, to=[to_email])
            # send_email.send()
            messages.success(request, 'Registration sucessful.')
            return redirect('Login')
    return render(request, 'acounts/register.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def Login(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request,user)
            if user.is_admin:
                return redirect('pdisplay')
            else:
                return redirect('home')
        else:
            return HttpResponse("email or password is incorrect")
        
        
    return render(request, 'acounts/login.html')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='Login')
def Logout(request):
    logout(request)
    return redirect('Login')


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def activate(request, uidb64, token):
    # try:
    #     uid= urlsafe_base64_decode(uidb64).decode()

    return HttpResponse('Ok')


# u = User.objects.get(username='vaisaghmp')
# u.set_password('123')
# u.save()


#----------RESET PASSWORD-----------
def change_password(request):
    context={}
    if request.method =='POST':
        current=request.POST["Current_password"]
        new=request.POST["New_password"]

        user=User.objects.get(id=request.user.id)
        check=user.check_password(current)

        if check==True:
            user.set_password(new)
            user.save()
            context['message'] = "Password changed successfully"
            context['col'] = "alert-success"

        else:
            context['message'] = "Incorrect current password"
            context['col'] = "alert-danger"

    return render(request,'change_password.html',context)

