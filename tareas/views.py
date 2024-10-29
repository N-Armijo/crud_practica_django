from django.shortcuts import render,redirect, get_object_or_404
from .models import Tarea

# Create your views here.
def create_tarea(request):
    if request.method =='POST':
        titulo=request.POST.get('titulo')
        descripcion=request.POST.get('descripcion')
        Tarea.objects.create(titulo=titulo,descripcion=descripcion)
        print()
        return redirect('listar_tareas')
    return render(request, 'create.html')

def listar_tareas(request):
    tareas=Tarea.objects.all()
    print(tareas)
    contexto={'tareas':tareas}
    return render(request,'listar_tareas.html',contexto)

def actualizar_tarea(request, id):
    tarea = get_object_or_404(Tarea,id=id)
    if request.method == 'POST':
        tarea.titulo = request.POST.get('titulo')
        tarea.descripcion = request.POST.get('descripcion')
        tarea.completado = request.POST.get('completado')
        tarea.save()
        return redirect('listar_tareas')
    return render(request, 'actualizar_tarea.html', {'tarea': tarea})

def eliminar_tarea(request,id):
    tarea = get_object_or_404(Tarea,id=id)
    if request.method == 'POST':
        tarea.delete()
        return redirect('listar_tareas')
    return render(request, 'eliminar_tarea.html', {'tarea': tarea})