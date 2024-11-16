from django.shortcuts import render, redirect
from .models import Libro
from .forms import LibroForm
from django.shortcuts import render

def home(request):
    return render(request, 'libros/home.html')


def lista_libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/lista.html', {'libros': libros})

def libro_detalle(request, pk):
    libro = Libro.objects.get(id=pk)
    return render(request, 'libros/detalle.html', {'libro': libro})

def libro_crear(request):
    if request.method == "POST":
        form = LibroForm(request.POST, request.FILES) 
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk) 
    else:
        form = LibroForm()  
    return render(request, 'libros/crear.html', {'form': form})
                  
def libro_editar(request, pk):
    libro = Libro.objects.get(pk=pk)
    if request.method == "POST":
        form = LibroForm(request.POST, instance=libro)
        if form.is_valid():
            libro = form.save()
            return redirect('libro_detalle', pk=libro.pk)
    else:
        form = LibroForm(instance=libro)
    return render(request, 'libros/editar.html', {'form': form})

def libro_eliminar(request, pk):
    libro = Libro.objects.get(pk=pk)
    libro.delete()
    return redirect('lista_libros')

# Create your views here.
