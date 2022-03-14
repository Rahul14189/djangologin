from django.shortcuts import render
from .models import Visitors

# To import builtin signup form
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        Visitors.objects.create(name = name, email = email)
        return render(request, 'home.html', context = {"msg": "Thank You! Your response has been recorded"})
 
    else:
        return render(request, 'home.html', context = None)

def aboutus(request):
    return render(request, 'about.html', context = None)

# def sign_up(request):
#     return render(request, 'sign_up.html', context = None)

# def logout(request):
#     return render(request, 'logout.html', context = None)

# def profile(request):
#     return render(request, 'profile.html', context = None)
