from django.urls import include, path
from . import  views
urlpatterns = [
path('cliente/', views.cliente, name='cliente'),
path('produto/', views.produto, name='produto'),
path('pedido/', views.pedido, name='pedido'),
path('imprimir/', views.imprimir, name='imprimir'),
path('delete_pedido/<int:id_pedido>/', views.delete_pedido, name='delete_pedido'),
path('edit_pedido/<int:id>/', views.edit_pedido, name='edit_pedido'),

]