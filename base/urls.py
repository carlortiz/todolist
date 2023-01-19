from django.urls import path
from .views import ShowTasks, CreateTask, EditTask, DeleteTask, LoginUser, RegisterUser
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', ShowTasks.as_view(), name='tasks'),
    path('create/', CreateTask.as_view(), name='create'),
    path('delete/<int:pk>', DeleteTask.as_view(), name='delete'),
    path('edit/<int:pk>/', EditTask.as_view(), name='edit'),
]
