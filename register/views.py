from django.shortcuts import render
from register.forms import RegisterForm
from register.models import Register
# Create your views here.

def register(request):
    # put the code here
    return render(request, 'register.html')