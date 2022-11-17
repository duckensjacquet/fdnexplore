from django.shortcuts import render
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your views here.

def Login(request):
    if request.method == 'POST':
        username=request.POST["username"]
        password=request.POST["password"]
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('dash'))
        else:
            return render(request, 'login/login.html', {'message': 'Invalid username or password'})
    return render(request, 'login/login.html')