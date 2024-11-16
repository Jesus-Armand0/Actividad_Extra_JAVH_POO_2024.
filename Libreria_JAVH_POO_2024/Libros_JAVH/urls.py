from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_libros, name='lista_libros'),
    path('libro/<int:pk>/', views.libro_detalle, name='libro_detalle'),
    path('libro/nuevo/', views.libro_crear, name='libro_crear'),
    path('libro/<int:pk>/editar/', views.libro_editar, name='libro_editar'),
    path('libro/<int:pk>/eliminar/', views.libro_eliminar, name='libro_eliminar'),
]
