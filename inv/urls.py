from django.urls import include, path 

from .views import CategoriaView, CategoriaNew

app_name = 'inv'  # Añade esta línea para definir el namespace

urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(), name='categoria_new'),

]   