from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView ,CreateView, UpdateView , DeleteView , DetailView, TemplateView
from .models import Task , Contact
from .forms import ContactForm


class CustomLoginView(LoginView):
    template_name= 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('home')

class CustomRegisterView(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self,form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super().form_valid(form)
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().get(*args, **kwargs)
def logout_view(request):
    logout(request)
    return redirect('login')

class HomeView(LoginRequiredMixin,ListView):
    template_name = 'home.html'
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        new_tasks=context['tasks'].filter(user=self.request.user)

        filter_type = self.request.GET.get('filter','all')
        if filter_type == "active":
            new_tasks=new_tasks.filter(is_complete=False)
        elif filter_type == "completed":
            new_tasks = new_tasks.filter(is_complete=True)
        context['tasks']=new_tasks
        context['filter_type']=filter_type

        return context

class TaskUpdateView(LoginRequiredMixin,UpdateView):
    template_name = 'task_update.html'
    model = Task
    def get_success_url(self):
        return reverse_lazy('home')
    fields = ['title','description', 'is_complete']

class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'task_create.html'
    fields = ['title','description', 'is_complete']

    def get_success_url(self):
        return reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TaskDeleteView(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('home')


class TaskDetailView(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'


class AboutTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'about.html'


class ContactTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'contact.html'

class ContactCreateView(LoginRequiredMixin,CreateView):
    model = Contact
    template_name = 'contact.html'
    form_class = ContactForm

    def get_success_url(self):
        return reverse_lazy('home')
