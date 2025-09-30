
from django.urls import path
from .views import *
urlpatterns = [
  path('',home,name="home"),
  path('login/',login_view,name="login"),
  path('register/',register_view,name="register"),
  path('logout/',logout_view,name="logout"),
  path('contact/',contact_view,name="contact"),
  path('about/',about_view,name="about"),


  path('task_create', task_create, name='task_create'),
  path('task_delete/<int:id>', task_delete, name='task_delete'),
  path('task_update/<int:id>', task_update, name='task_update'),
]
