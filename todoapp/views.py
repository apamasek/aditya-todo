from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import RegistrationForm, TaskForm
from .models import Task



class HomeView(TemplateView):
    template_name = 'dashboard.html'

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect('dashboard')
        else:
            return HttpResponseRedirect('accounts/login')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

    def get(self, request):
        form = RegistrationForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            # mengambil input dari form
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect(reverse('dashboard'))
        else:
            return render(request, self.template_name, {'form':form})

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'

    def post(self, request):
         # query task yang statusnya 0 = Not Completed
        tasks = Task.objects.filter(status=0).order_by('id')
        return render(request, self.template_name, {'tasks': tasks })

class TaskAllView(LoginRequiredMixin,ListView):
    model = Task
    template_name = 'task/task_list.html'

class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'task/task_detail.html'

class TaskAddView(LoginRequiredMixin, TemplateView):
    template_name = 'task/task_form.html'

    def get(self, request):
        form = TaskForm()
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Task successfully added")
            return HttpResponseRedirect(reverse('task-list'))
        else:
            messages.error(request, "Please correct your input")
            return render(request, self.template_name, {'form':form})