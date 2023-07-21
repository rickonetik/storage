from django import forms
from myapp.models import (
    Supplier, Employee, Product, Order,
    Inventory, PurchaseOrder, ShipmentOrder
)

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'email', 'phone', 'is_active']

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['username', 'password']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'order_quantity', 'order_status']

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ['product', 'stock_quantity']

class PurchaseOrderForm(forms.ModelForm):
    class Meta:
        model = PurchaseOrder
        fields = ['product', 'quantity', 'status']

class ShipmentOrderForm(forms.ModelForm):
    class Meta:
        model = ShipmentOrder
        fields = ['product', 'quantity', 'status']