from django import forms
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Task
from .forms import RegisterForm

# Create your views here.


class ShowTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(user=self.request.user)
        context['count'] = context['tasks'].filter(completed=False).count()

        search_input = self.request.GET.get('search-bar')
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        return context


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
       form.instance.user = self.request.user
       return super().form_valid(form)


class EditTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')


class LoginUser(LoginView):
    template_name = "base/login.html"
    next_page = 'tasks'


class RegisterUser(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = "base/register.html"
  

