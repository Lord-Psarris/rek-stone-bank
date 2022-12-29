from django.shortcuts import render, redirect


# Create your views here.
def home(requests):
    if requests.user.is_authenticated:
        return redirect('dashboard:home')
        
    return render(requests, 'main/index.html')
