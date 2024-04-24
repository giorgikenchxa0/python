from django.shortcuts import render
from django.http import HttpRequest , HttpResponse
from django.views.generic import CreateView , DetailView
from users.forms import UserCreationForm
from django.urls import reverse_lazy
from users.models import User
# Create your views here.

class UserCreateView(CreateView):
    success_url = reverse_lazy('sign_in')
    template_name = 'user/user_creation.html'
    form_class = UserCreationForm
    
    

class profileview(DetailView):
    template_name = 'user/profile.html'
    model = User



