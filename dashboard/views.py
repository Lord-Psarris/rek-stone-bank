from django.shortcuts import render


# Create your views here.
def home(requests):
    return render(requests, 'dashboard/home.html')


def transactions(requests):
    return render(requests, 'dashboard/transactions.html')


def profile(requests):
    return render(requests, 'dashboard/profile.html')
