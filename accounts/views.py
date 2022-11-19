from django.shortcuts import render


# Create your views here.
def login(requests):
    return render(requests, 'accounts/login.html')


def register(requests):
    return render(requests, 'accounts/register.html')
