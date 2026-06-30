from django.contrib import admin
from .models import Category, Supplier, Product, StockIn, StockOut


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "created_at",
    )

    search_fields = (
        "name",
    )

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):

    list_display = (
        "company",
        "name",
        "phone",
        "city",
    )

    search_fields = (
        "company",
        "name",
    )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "code",
        "name",
        "category",
        "supplier",
        "stock",
        "status",

    )

    search_fields = (
        "code",
        "name",

    )

    list_filter = (
        "category",
        "supplier",
        "status",

    )

@admin.register(StockIn)
class StockInAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "product",
        "supplier",
        "quantity",
        "price",
    )

    search_fields = (
        "product__name",
        "invoice",
    )

    list_filter = (
        "supplier",
        "date",
    )

@admin.register(StockOut)
class StockOutAdmin(admin.ModelAdmin):

    list_display = (
        "date",
        "product",
        "receiver",
        "quantity",
    )

    search_fields = (
        "product__name",
        "invoice",
        "receiver",
    )

    list_filter = (
        "date",
    )