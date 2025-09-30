from django.urls import path
from .views import *


urlpatterns = [
    path('login/',CustomLoginView.as_view(),name='login'),
    path('register/',CustomRegisterView.as_view(),name='register'),
    path('logout/', logout_view,name='logout'),
    path('',HomeView.as_view(),name='home'),
    path('about/',AboutTemplateView.as_view(),name='about'),
    path('contact',ContactCreateView.as_view(),name='contact'),
    path('task/<int:pk>',TaskDetailView.as_view(),name='task'),
    path('create/',TaskCreateView.as_view(),name='create'),
    path('update/<int:pk>',TaskUpdateView.as_view(),name='update'),
    path('delete/<int:pk>',TaskDeleteView.as_view(),name='delete'),

]
