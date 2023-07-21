# myapp/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from myapp.forms import (
    SupplierForm, EmployeeForm, ProductForm, OrderForm,
    InventoryForm, PurchaseOrderForm, ShipmentOrderForm
)
from myapp.models import (
    Supplier, Employee, Product, Order
)
from django.contrib.auth.models import User

def initial_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            # Handle invalid login
            pass
    return render(request, 'initial_page.html')

@login_required
def main_page(request):
    return render(request, 'main_page.html')

@login_required
def supplier_list_view(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier_list.html', {'suppliers': suppliers})

@login_required
def add_supplier_view(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new supplier to the database
            return redirect('supplier_list')  # Redirect to the supplier list view
    else:
        form = SupplierForm()

    return render(request, 'add_supplier.html', {'form': form})

@login_required
def delete_supplier_view(request, supplier_pk):
    supplier = get_object_or_404(Supplier, pk=supplier_pk)
    if request.method == 'POST':
        supplier.delete()
        return redirect('supplier_list')
    return render(request, 'delete_supplier.html', {'supplier': supplier})

@login_required
def employee_list_view(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

@login_required
def add_employee_view(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            # Save the employee object
            employee = form.save()

            # Create a superuser with the employee's credentials
            user = User.objects.create_superuser(username=employee.username, password=form.cleaned_data['password'])
            
            # Log in the new superuser
            user = authenticate(request, username=employee.username, password=form.cleaned_data['password'])
            login(request, user)

            return redirect('employee_list')
    else:
        form = EmployeeForm()

    return render(request, 'add_employee.html', {'form': form})
@login_required
def delete_employee_view(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()
    return redirect('employee_list')
@login_required
def initial_page_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('employee_list')
        else:
            return render(request, 'initial_page.html', {'error_message': 'Invalid login credentials'})

    return render(request, 'initial_page.html')



@login_required
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

@login_required
def add_product_view(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()

    return render(request, 'add_product.html', {'form': form})

@login_required
def edit_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')

    return render(request, 'delete_product.html', {'product': product})

@login_required
def order_list_view(request):
    orders = Order.objects.all()
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def add_order_view(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            product = order.product
            if order.order_quantity <= product.quantity:
                order.save()
                return redirect('order_list')
            else:
                form.add_error('order_quantity', f"Количество не может быть больше {product.quantity}.")
    else:
        form = OrderForm()

    return render(request, 'add_order.html', {'form': form})

@login_required
def edit_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')
    else:
        form = OrderForm(instance=order)

    return render(request, 'edit_order.html', {'form': form, 'order': order})

@login_required
def delete_order_view(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    if request.method == 'POST':
        order.delete()
        return redirect('order_list')

    return render(request, 'delete_order.html', {'order': order})

