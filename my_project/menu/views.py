from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

@login_required
def welcome(request):
    return render(request, 'home.html')