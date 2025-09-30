
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import  messages
from django.http import JsonResponse

from .forms import TaskForm
from .models import Task



@login_required
def home(request):
  filter_type = request.GET.get('filter', 'all')
  if filter_type == "active":
    tasks = Task.objects.filter(complete=False)
  elif filter_type == "complete":
    tasks = Task.objects.filter(complete=True)
  else:
    tasks = Task.objects.all()
  return render(request, 'home.html', {'tasks': tasks, 'filter_type': filter_type})


def task_create(request):
  if request.method == "POST":
    form = TaskForm(request.POST)
    if form.is_valid():
      task =form.save(commit=False)
      task.user=request.user
      task.save()
      return JsonResponse({
        "status": "success",
        "task": {
          "id": task.id,
          "title": task.title,
          "description": task.description,
          "complete": task.complete,
        }
      }, status=201)
    else:
      return JsonResponse({
        "status": "error",
        "errors": form.errors
      }, status=400)

  return JsonResponse({"status": "invalid method"}, status=405)

def task_delete(request,id):
  task_to_delete = Task.objects.filter(user=request.user,id=id)
  if task_to_delete:
    task_to_delete.delete()
    return redirect('home')
  return redirect('home')

def task_update(request,id):
  if request.method == "POST":
    task = get_object_or_404(Task,id=id)
    form = TaskForm(request.POST,instance=task)
    if form.is_valid():
      form.save()
      return JsonResponse({"status": "success"}, status=200)
    else:
      return JsonResponse({"status": "error", "errors": form.errors}, status=400)

  return JsonResponse({"status": "invalid method"}, status=405)












def logout_view(request):
  logout(request)
  return redirect('login')

def login_view(request):
  if request.user.is_authenticated:
    return redirect('home')
  if request.method == 'POST':
    username=request.POST.get('username')
    password=request.POST.get('password')
    validate_user=authenticate(username=username,password=password)
    if validate_user:
      login(request,validate_user)
      return redirect('home')
    else:
      messages.error(request,'Error, wrong user details or user does not exist')
      messages.error(request,'Error, wrong user details or user does not exist2')
      return render(request,'login.html')

  return render(request,'login.html',{})




def register_view(request):
  return render(request,'register.html',{})
def contact_view(request):
  return render(request,'contact.html',{})
def about_view(request):
  return render(request,'about.html',{})