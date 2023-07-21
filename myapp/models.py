# myapp/models.py

from django.db import models
from django.contrib.auth.models import BaseUserManager


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.TextField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('On the stock', 'На складе'),
        ('Shipped', 'Отправлено'),
        ('Delivered', 'Доставлено'),
    ]

    product = models.ForeignKey(Product, on_delete=models.CASCADE, default='')
    order_quantity = models.PositiveIntegerField(default=1)
    order_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='On the stock')

    def __str__(self):
        return f"{self.product.name} - {self.get_order_status_display()}"

class Employee(models.Model):
    username = models.CharField(max_length=100, unique=True, default='')
    password = models.CharField(max_length=100, default='')

class EmployeeManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError("Поле Имя пользователя должно быть задано")
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(username, password, **extra_fields)

class Supplier(models.Model):
    name = models.CharField(max_length=100, default='')
    email = models.EmailField(default='')
    phone = models.CharField(max_length=15, default='')
    is_active = models.BooleanField(default=True)

class Inventory(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.stock_quantity} units"
    
class PurchaseOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Completed', 'Completed')])

    def __str__(self):
        return f"Purchase Order - {self.product.name} x {self.quantity} ({self.status})"

class ShipmentOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Shipped', 'Shipped')])

    def __str__(self):
        return f"Shipment Order - {self.product.name} x {self.quantity} ({self.status})"