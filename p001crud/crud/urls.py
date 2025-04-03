from django.urls import path
from .import views
#se define el nombre a la url ya que se manejan por cvistas y la que tiene acceso ala aplicacion
app_name = 'crud'

urlpatterns = [
    path('',views.task_list_and_create, name='crud_list'),
    path('update_task/<int:task_id>',views.update_tasks, name='update_task'),
    path('edit_task/<int:task_id>',views.edit_task, name='edit_task'),
    path('delete_task/<int:task_id>',views.delete_task, name='delete_task'),
]