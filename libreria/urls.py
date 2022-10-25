from django.urls import path
from . import views

urlpatterns= [
    path('', views.inicio, name="inicio"),
    path('nosotros', views.nosotros, name="nosotros"),
    path('libros', views.libros, name="libros"),
    path('crear-libro', views.crear, name="crear"),
    path('editar-libro', views.editar, name="editar"),
]