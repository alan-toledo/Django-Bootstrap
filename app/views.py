from django.shortcuts import render
from django.views.generic import ListView
from .models import Task, User
from .forms import UserForm, TaskForm
from django.shortcuts import redirect
from django.contrib import messages

class UserListView(ListView):
    model = User
    template_name = 'users.html'
    
    def get_queryset(self):
        return User.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    
    def get_queryset(self):
        return Task.objects.filter(user__pk=self.kwargs['user_id']).order_by('status').order_by('priority').order_by('-date')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Welcome'
        context['user'] =  User.objects.filter(id=self.kwargs['user_id']).get()
        context['task_id'] = self.kwargs['task_id']
        try:
            task = Task.objects.filter(id = self.kwargs['task_id']).get()
            context['form'] = TaskForm(instance = task)
        except Task.DoesNotExist:
            context['form'] =  TaskForm()
        return context
    
def user(request):
    form = UserForm()
    return render(request, 'user.html', {'form': form})

def login(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.filter(email = email).get()
                password = form.cleaned_data['password']
                if password == user.password:
                    return redirect('tasks', **{'user_id': user.id})
                else:
                    messages.info(request, 'Invalid credentials')
                    return render(request, 'user.html', {'form': form})
            except User.DoesNotExist:
                user = form.save()
                return redirect('tasks', **{'user_id': user.id})
        else:
            messages.info(request, 'Invalid Input')
            return render(request, 'user.html', {'form': form})

def add_task(request,  **kwargs):
    if request.method == "POST":
        user = User.objects.get(id = kwargs['user_id'])
        form = TaskForm(request.POST, instance = Task(user = user))
        if form.is_valid():
            form.save()
            return redirect('tasks', **{'user_id': user.id})
        else:
            messages.info(request, 'Invalid Input')
            return redirect('tasks', **{'user_id': user.id})

def delete_task(request, **kwargs):
    if request.method == "POST":
        task = Task.objects.get(id = kwargs['task_id'])
        task.delete()
        return redirect('tasks', **{'user_id': kwargs['user_id']})

def edit_task(request, user_id = None, task_id = None):
    if request.method == "GET":
        return redirect('tasks', **{'user_id': user_id, 'task_id': task_id})
    if request.method == "POST":
        task = Task.objects.get(id = task_id)
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('tasks', **{'user_id': user_id})
        else:
            messages.info(request, 'Invalid Input')
            return redirect('tasks', **{'user_id': user_id})