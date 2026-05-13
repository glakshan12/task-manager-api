from django.urls import path
from .views import RegisterView, LoginView, TaskListCreateView, TaskDetailView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),#for register
    path('login/', LoginView.as_view(), name='login'),#for login
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),#for create and view
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),# for delete, retrive and update
]
