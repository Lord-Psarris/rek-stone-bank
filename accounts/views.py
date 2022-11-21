from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse

from .models import Users


# Create your views here.
def login(requests):

    # collect details on post request
    if requests.POST:
        print('here')
        password = requests.POST['password']
        email = requests.POST['email']

        # verify the email exists
        if Users.objects.filter(email=email).count() == 0:
            messages.error(requests, 'Email doesn\'t exist in our database')

        # verify username and password
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(requests, user)

            if requests.GET.get('next'):
                return HttpResponseRedirect(requests.GET.get('next'))
            return HttpResponseRedirect(reverse('dashboard:home'))

        messages.error(requests, 'Incorrect email or password')
        return HttpResponseRedirect(reverse('accounts:login'))


    return render(requests, 'accounts/login.html')


def register(requests):
    return render(requests, 'accounts/register.html')


def logout(requests):
    auth.logout(requests)
    return redirect('main:home')
