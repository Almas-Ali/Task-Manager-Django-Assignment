from django.urls import path
from django.contrib.auth.views import LogoutView

from tasks import views

app_name = 'tasks'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('tasks/', views.TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/create/', views.TaskCreateView.as_view(), name='task_create'),
    path('tasks/update/<int:pk>/', views.TaskUpdateView.as_view(), name='task_update'),
    path('tasks/search/', views.TaskSearchView.as_view(), name='task_search'),
    
    # API views
    path('api/tasks/create/', views.TaskListCreateAPIView.as_view(), name='api_task_list_create'),
    path('api/tasks/update/<int:pk>/', views.TaskUpdateAPIView.as_view(), name='api_task_update'),
    path('api/tasks/delete/<int:pk>/', views.TaskDestroyAPIView.as_view(), name='api_task_delete'),
    path('api/login/', views.LoginAPIView.as_view(), name='api_login'),
]
