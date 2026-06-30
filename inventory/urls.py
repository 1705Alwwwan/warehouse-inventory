from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # ==========================
    # SUPPLIER
    # ==========================

    path("category/", views.category_list,name="category_list"),
    path("category/add/",views.category_add,name="category_add"),
    path("category/<int:pk>/edit/", views.category_edit, name="category_edit"),
    path("category/<int:pk>/delete/", views.category_delete, name="category_delete"),

    # ==========================
    # SUPPLIER
    # ==========================
    path("supplier/", views.supplier_list, name="supplier_list"),
    path("supplier/add/", views.supplier_add, name="supplier_add"),
    path("supplier/<int:pk>/edit/", views.supplier_edit, name="supplier_edit"),
    path("supplier/<int:pk>/delete/", views.supplier_delete, name="supplier_delete"),

    # ==========================
    # PRODUCT
    # ==========================

    path(
        "product/",
        views.product_list,
        name="product_list",
    ),

    path(
        "product/add/",
        views.product_add,
        name="product_add",
    ),

    path(
        "product/<int:pk>/edit/",
        views.product_edit,
        name="product_edit",
    ),

    path(
        "product/<int:pk>/delete/",
        views.product_delete,
        name="product_delete",
    ),

    # ==========================
    # STOCK IN
    # ==========================

    path(
        "stockin/",
        views.stockin_list,
        name="stockin_list",
    ),

    path(
        "stockin/add/",
        views.stockin_add,
        name="stockin_add",
    ),

    path(
        "stockin/<int:pk>/edit/",
        views.stockin_edit,
        name="stockin_edit",
    ),

    path(
        "stockin/<int:pk>/delete/",
        views.stockin_delete,
        name="stockin_delete",
    ),

    # ==========================================
    # STOCK OUT
    # ==========================================

    path(
        "stockout/",
        views.stockout_list,
        name="stockout_list",
    ),

    path(
        "stockout/add/",
        views.stockout_add,
        name="stockout_add",
    ),

    path(
        "stockout/<int:pk>/edit/",
        views.stockout_edit,
        name="stockout_edit",
    ),

    path(
        "stockout/<int:pk>/delete/",
        views.stockout_delete,
        name="stockout_delete",
    ),

    # ==========================================
    # REPORT
    # ==========================================

    path(
    "reports/stock/",
    views.report_stock,
    name="report_stock",
    ),
    path(
    "reports/stockin/",
    views.report_stockin,
    name="report_stockin",
    ),
    path(
    "reports/stockout/",
    views.report_stockout,
    name="report_stockout",
    ),
]