from django.urls import path
from ventas import views
#from .views import home_page_view, carrito, formulario_pedido, product_model_detail_view

urlpatterns = [
    path('productos/', views.home_page_view, name='productos'),
    path('carrito/', views.carrito, name="carrito"),
    path('formulario/', views.formulario_pedido, name="formulario"),
    path("productos/<int:product_id>", views.product_model_detail_view, name="detail"),
]