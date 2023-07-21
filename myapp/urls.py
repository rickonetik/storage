from django.urls import path
from . import views

urlpatterns = [
    path('', views.initial_page, name='initial_page'),
    path('main/', views.main_page, name='main_page'),
    path('suppliers/', views.supplier_list_view, name='supplier_list'),
    path('suppliers/add/', views.add_supplier_view, name='add_supplier'),
    path('suppliers/delete/<int:supplier_pk>/', views.delete_supplier_view, name='delete_supplier'),
    path('employees/', views.employee_list_view, name='employee_list'),
    path('employees/add/', views.add_employee_view, name='add_employee'),
    path('employees/delete/<int:employee_id>/', views.delete_employee_view, name='delete_employee'),
    path('product_list/', views.product_list_view, name='product_list'),
    path('add_product/', views.add_product_view, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product_view, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product_view, name='delete_product'),
    path('order_list/', views.order_list_view, name='order_list'),
    path('add_order/', views.add_order_view, name='add_order'),
    path('edit_order/<int:order_id>/', views.edit_order_view, name='edit_order'),
    path('delete_order/<int:order_id>/', views.delete_order_view, name='delete_order'),
]