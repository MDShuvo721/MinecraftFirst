from django.urls import path
from . import views

app_name = 'WorldTasks'
urlpatterns = [
    path('worlds/', views.worlds, name='worlds_list'),
    path('create_world/', views.create_world, name='create_world'),
    path('tasks/<int:world_id>/', views.show_task, name='show_task'),
    path('complete/<int:world_task_id>/', views.complete_task, name='complete_task'),
    path('fail/<int:world_task_id>/', views.fail_task, name='fail_task'),
    path('delete/<int:world_id>/', views.delete_world, name='delete_world'),
]
