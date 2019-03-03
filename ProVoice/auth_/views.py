from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile

# Create your views here.
def register(request):
    form = UserCreationForm(data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'auth_/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            auth.login(request, user)
            return redirect('index')
        else:
            error = "username or password incorrect"
            return render(request, 'auth_/login.html', {'error': error})
    else:
        return render(request, 'auth_/login.html')


def logout(request):
    auth.logout(request)
    return redirect('index')

class ProfileView(CreateView, LoginRequiredMixin):
    model = Profile
    fields = ('is_teacher', 'is_student', 'age', 'rating')
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.save()
        return super().form_valid(form)

class ProfileListView(ListView, LoginRequiredMixin):
    model = Profile
    context_object_name = 'profiles'  