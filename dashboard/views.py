from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from .models import *

# getting auth url
AUTH_URL = settings.AUTH_URL


# Create your views here.
@login_required(login_url=AUTH_URL)
def home(requests):
    # get transactions
    transactions = Transactions.objects.filter(client=requests.user).all()[:10]

    return render(requests, 'dashboard/home.html', {"transactions": transactions})


@login_required(login_url=AUTH_URL)
def transactions(requests):
    # get transactions
    transactions = Transactions.objects.filter(client=requests.user).all()

    return render(requests, 'dashboard/transactions.html', {"transactions": transactions})


@login_required(login_url=AUTH_URL)
def profile(requests):
    return render(requests, 'dashboard/profile.html')
