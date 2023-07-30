from django.contrib import admin
from .models import Product, Cart, OrderPlaced
from django.contrib.auth.models import User

# Register your models here




@admin.register(Product)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'selling_price', 'discounted_price', 'discription', 'brand', 'category', 'product_img']

@admin.register(Cart)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'product', 'quantity']

@admin.register(OrderPlaced)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['id','user', 'location', 'name', 'phone_number', 'state', 'product', 'quantity', 'ordered_date', 'status', 'payment_method']