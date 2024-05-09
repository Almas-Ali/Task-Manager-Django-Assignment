from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, DestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.response import Response
from rest_framework import status

from tasks.models import Task
from tasks.forms import TaskCreationForm, TaskUpdateForm
from tasks.serializers import TaskSerializer


class IndexView(TemplateView):
    template_name = 'index.html'


class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        return Task.objects.all().order_by('-created_at')


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'tasks/detail.html'
    context_object_name = 'task'


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskCreationForm
    template_name = 'tasks/create.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskUpdateForm
    template_name = 'tasks/update.html'
    success_url = reverse_lazy('tasks:task_list')


class TaskListCreateAPIView(CreateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class TaskUpdateAPIView(UpdateAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class TaskDestroyAPIView(DestroyAPIView):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    permission_classes = [IsAuthenticated]


class LoginView(TemplateView):
    template_name = 'login.html'


class LoginAPIView(APIView):
    authentication_classes = [BasicAuthentication, SessionAuthentication]

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class TaskSearchView(LoginRequiredMixin, TemplateView):
    template_name = 'tasks/search.html'

    def get(self, request):
        query = request.GET.get('q', '')
        if len(query) > 50 or len(query) < 1:
            # database search is expensive, so we limit the search query
            return render(request, 'tasks/search.html', {'search_task': []})

        filter = request.GET.get('filter', 'created_at')
        # checking if the filter is valid
        if filter not in [
            'title',
            '-title',
            'created_at',
            '-created_at',
            'due_date',
            '-due_date',
            'priority',
            '-priority',
            'is_completed',
            '-is_completed',
        ]:
            filter = 'created_at'

        task = Task.objects.filter(title__icontains=query).order_by(filter)

        return render(request, 'tasks/search.html', {'search_task': task})
