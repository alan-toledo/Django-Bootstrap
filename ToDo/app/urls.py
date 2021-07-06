from django.urls import path

from . import views

urlpatterns = [
    path('', views.user, name='index'),
    path('users/', views.UserListView.as_view(), name='users'),
    path('user/', views.login, name='user'),
    path('user/<int:user_id>/task/add/', views.add_task, name='add'),
    path('user/<int:user_id>/task/delete/<int:task_id>/', views.delete_task, name='delete'),
    path('user/<int:user_id>/task/edit/<int:task_id>/', views.edit_task, name='edit'),
    path('user/<int:user_id>/task/', views.TaskListView.as_view(), {'task_id': 0}, name='tasks'),
    path('user/<int:user_id>/task/<int:task_id>/', views.TaskListView.as_view(), name='tasks'),
]