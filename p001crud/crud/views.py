from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm
#recibe la request y el objeto que se va a crear
    #para acceder a li importante de la base de datos

#Metodo para GUARDAR y LISTAR las tareas
def task_list_and_create(request):
    
    if request.method == 'POST':
        form = TaskForm(request.POST )
        if form.is_valid():
            #se guarda el objeto en la base de datos
            form.save()
            #se vuelve a cargar la pagina/esta en la de urls
            return redirect('crud:crud_list')
    else:
                form = TaskForm()
    #tasks = Task.objects.all()
    complete_tasks = Task.objects.filter(is_completed=True)
    incomplete_tasks = Task.objects.filter(is_completed=False)

    
    #se define que archivo html se usara y lo que se mandara con un diccionario
    return render(request, 'task_list.html',{
        'form': form,
        #'tasks': tasks
        'complete_tasks': complete_tasks,
        'incomplete_tasks': incomplete_tasks,
    })
    
#Metodo para ACTUALIZAR tarea
def update_tasks(request, task_id):
    #se busca el objeto a modificar
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.is_completed = not task.is_completed
        task.save()
        return redirect('crud:crud_list')
    
#Metodo para EDITAR tarea/ cuidar la sintasix
def edit_task(requests, task_id):
    task = get_object_or_404(Task, id=task_id)
    initial_data = {
        'title': task.title,
        'description': task.description,
    }
    
    if requests.method == 'POST':
        form = TaskForm(requests.POST, instance=task)
        #se guarda el objeto en la base de datos
        #se verifica si el formulario es valido
        if form.is_valid():
            form.save()
            return redirect('crud:crud_list')
        else:
            form = TaskForm(instance=task,initial=initial_data)
            #no olvidar comillas
    return render(requests, 'edit_task.html', {'form': form})

#Metodo para ELIMINAR tarea
def delete_task(request, task_id):
    if request.method == 'POST':
        task = Task.objects.get(id=task_id)
        task.delete()
        return redirect('crud:crud_list')



