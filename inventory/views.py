from django.shortcuts import render, redirect, get_object_or_404
from django.db import models
from .models import Category, Supplier, Product, StockIn, StockOut
from .forms import CategoryForm, SupplierForm, ProductForm, StockInForm, StockOutForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from django.db.models import Q
from django.db.models import F
from datetime import datetime


@login_required
def dashboard(request):

    total_product = Product.objects.count()

    total_supplier = Supplier.objects.count()

    total_stockin = (
        StockIn.objects.aggregate(
            total=Sum("quantity")
        )["total"] or 0
    )

    total_stockout = (
        StockOut.objects.aggregate(
            total=Sum("quantity")
        )["total"] or 0
    )

    total_stock = (
        Product.objects.aggregate(
            total=Sum("stock")
        )["total"] or 0
    )

    low_stock = Product.objects.filter(
        stock__lte=models.F("minimum_stock")
    )

    context = {

        "total_product": total_product,

        "total_supplier": total_supplier,

        "total_stockin": total_stockin,

        "total_stockout": total_stockout,

        "total_stock": total_stock,

        "low_stock_count": low_stock.count(),

        "low_stock": low_stock,

    }

    return render(
        request,
        "dashboard.html",
        context,
    )

#===========================================================================
#CATEGORY===================================================================
#===========================================================================

@login_required
def category_list(request):

    keyword = request.GET.get("q", "")

    categories = Category.objects.all()

    if keyword:

        categories = categories.filter(

            Q(name__icontains=keyword) |
            Q(description__icontains=keyword)

        )

    context = {

        "categories": categories,
        "keyword": keyword,

    }

    return render(
        request,
        "category/list.html",
        context,
    )


@login_required
def category_add(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Kategori berhasil ditambahkan.")
        return redirect("category_list")
    return render(
        request,
        "category/form.html",
        {
            "form": form,
            "title": "Tambah Kategori",
        },
    )

@login_required
def category_edit(request, pk):

    category = get_object_or_404(Category, pk=pk)

    form = CategoryForm(
        request.POST or None,
        instance=category
    )

    if form.is_valid():
        form.save()
        messages.success(request, "Kategori berhasil diperbarui.")
        return redirect("category_list")

    return render(
        request,
        "category/form.html",
        {
            "form": form,
            "title": "Edit Kategori",
        },
    )

@login_required
def category_delete(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":

        category.delete()
        messages.success(
            request,
            "Kategori berhasil dihapus."
        )

        return redirect("category_list")

    return render(
        request,
        "category/delete.html",
        {
            "category": category
        },
    )

#===========================================================================
#SUPPLIER===================================================================
#===========================================================================
@login_required
def supplier_list(request):

    keyword = request.GET.get("q", "")

    suppliers = Supplier.objects.all()

    if keyword:

        suppliers = suppliers.filter(

            Q(company__icontains=keyword) |
            Q(pic__icontains=keyword) |
            Q(phone__icontains=keyword) |
            Q(email__icontains=keyword)

        )

    context = {

        "suppliers": suppliers,
        "keyword": keyword,

    }

    return render(
        request,
        "supplier/list.html",
        context,
    )

@login_required
def supplier_add(request):
    form = SupplierForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "supplier berhasil ditambahkan!")
        return redirect("supplier_list")
    context ={"form":form,"title":"tambah supplier!"}
    return render(request, "supplier/form.html", context)


@login_required
def supplier_edit(request,pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    form = SupplierForm(
    request.POST or None,
    instance=supplier
    )
    if form.is_valid():
        form.save()
        messages.success(request, "Supplier behasil disimpan!")
        return redirect ("supplier_list")
    context = {"form":form, "title": "edit supplier" }
    return render(request, "supplier/form.html", context)

@login_required
def supplier_delete(request, pk):
    supplier = get_object_or_404(
                Supplier,
                pk=pk
            )
    if request.method == "POST":
        supplier.delete()
        messages.success(request, "supplier berhasil dihapus!")
        return redirect("supplier_list")
    context = {"supplier":supplier}
    return render(request, "supplier/delete.html", context)

#===========================================================================
#PRODUCT====================================================================
#===========================================================================
@login_required
def product_list(request):

    keyword = request.GET.get("q", "")

    products = Product.objects.select_related(
        "category",
        "supplier"
    ).all()

    if keyword:

        products = products.filter(

            Q(code__icontains=keyword) |
            Q(name__icontains=keyword) |
            Q(category__name__icontains=keyword) |
            Q(supplier__company__icontains=keyword)

        )

    context = {

        "products": products,
        "keyword": keyword,

    }

    return render(
        request,
        "product/list.html",
        context,
    )


@login_required
def product_add(request):

    form = ProductForm(
        request.POST or None,
        request.FILES or None,
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Product berhasil ditambahkan."
        )

        return redirect("product_list")

    context = {
        "form": form,
        "title": "Tambah Product",
    }

    return render(
        request,
        "product/form.html",
        context,
    )


@login_required
def product_edit(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product,
    )

    if form.is_valid():

        form.save()

        messages.success(
            request,
            "Product berhasil diperbarui."
        )

        return redirect("product_list")

    context = {
        "form": form,
        "title": "Edit Product",
    }

    return render(
        request,
        "product/form.html",
        context,
    )


@login_required
def product_delete(request, pk):

    product = get_object_or_404(
        Product,
        pk=pk,
    )

    if request.method == "POST":

        product.delete()

        messages.success(
            request,
            "Product berhasil dihapus."
        )

        return redirect("product_list")

    context = {
        "product": product,
    }

    return render(
        request,
        "product/delete.html",
        context,
    )

#===========================================================================
#STOCK IN===================================================================
#===========================================================================
@login_required
def stockin_list(request):

    keyword = request.GET.get("q", "")

    stockins = StockIn.objects.select_related(
        "product",
        "supplier"
    )

    if keyword:

        stockins = stockins.filter(

            Q(invoice__icontains=keyword) |
            Q(product__name__icontains=keyword) |
            Q(supplier__company__icontains=keyword)

        )

    context = {

        "stockins": stockins,
        "keyword": keyword,

    }

    return render(
        request,
        "stockin/list.html",
        context,
    )


@login_required
def stockin_add(request):

    form = StockInForm(request.POST or None)

    if form.is_valid():

        stockin = form.save(commit=False)

        product = stockin.product

        product.stock += stockin.quantity

        product.save()

        stockin.save()

        messages.success(
            request,
            "Barang masuk berhasil ditambahkan."
        )

        return redirect("stockin_list")

    context = {
        "form": form,
        "title": "Tambah Barang Masuk",
    }

    return render(
        request,
        "stockin/form.html",
        context,
    )


@login_required
def stockin_edit(request, pk):

    stockin = get_object_or_404(
        StockIn,
        pk=pk,
    )

    old_qty = stockin.quantity

    form = StockInForm(
        request.POST or None,
        instance=stockin,
    )

    if form.is_valid():

        stockin = form.save(commit=False)

        product = stockin.product

        # kembalikan stok lama
        product.stock -= old_qty

        # tambahkan stok baru
        product.stock += stockin.quantity

        product.save()

        stockin.save()

        messages.success(
            request,
            "Barang masuk berhasil diperbarui."
        )

        return redirect("stockin_list")

    context = {
        "form": form,
        "title": "Edit Barang Masuk",
    }

    return render(
        request,
        "stockin/form.html",
        context,
    )


@login_required
def stockin_delete(request, pk):

    stockin = get_object_or_404(
        StockIn,
        pk=pk,
    )

    if request.method == "POST":

        product = stockin.product

        # kurangi stok
        product.stock -= stockin.quantity

        product.save()

        stockin.delete()

        messages.success(
            request,
            "Barang masuk berhasil dihapus."
        )

        return redirect("stockin_list")

    context = {
        "stockin": stockin,
    }

    return render(
        request,
        "stockin/delete.html",
        context,
    )


#===========================================================================
#STOCK OUT==================================================================
#===========================================================================

@login_required
def stockout_list(request):

    keyword = request.GET.get("q", "")

    stockouts = StockOut.objects.select_related(
        "product"
    )

    if keyword:

        stockouts = stockouts.filter(

            Q(invoice__icontains=keyword) |
            Q(product__name__icontains=keyword) |
            Q(receiver__icontains=keyword)

        )

    context = {

        "stockouts": stockouts,
        "keyword": keyword,

    }

    return render(
        request,
        "stockout/list.html",
        context,
    )


@login_required
def stockout_add(request):

    form = StockOutForm(request.POST or None)

    if form.is_valid():

        stockout = form.save(commit=False)

        product = stockout.product

        if product.stock < stockout.quantity:

            messages.error(
                request,
                "Stok tidak mencukupi."
            )

        else:

            product.stock -= stockout.quantity

            product.save()

            stockout.save()

            messages.success(
                request,
                "Barang keluar berhasil ditambahkan."
            )

            return redirect("stockout_list")

    context = {
        "form": form,
        "title": "Tambah Barang Keluar",
    }

    return render(
        request,
        "stockout/form.html",
        context,
    )


@login_required
def stockout_edit(request, pk):

    stockout = get_object_or_404(
        StockOut,
        pk=pk,
    )

    old_qty = stockout.quantity

    form = StockOutForm(
        request.POST or None,
        instance=stockout,
    )

    if form.is_valid():

        stockout = form.save(commit=False)

        product = stockout.product

        # kembalikan stok lama
        product.stock += old_qty

        if product.stock < stockout.quantity:

            messages.error(
                request,
                "Stok tidak mencukupi."
            )

        else:

            product.stock -= stockout.quantity

            product.save()

            stockout.save()

            messages.success(
                request,
                "Barang keluar berhasil diperbarui."
            )

            return redirect("stockout_list")

    context = {
        "form": form,
        "title": "Edit Barang Keluar",
    }

    return render(
        request,
        "stockout/form.html",
        context,
    )


@login_required
def stockout_delete(request, pk):

    stockout = get_object_or_404(
        StockOut,
        pk=pk,
    )

    if request.method == "POST":

        product = stockout.product

        # kembalikan stok

        product.stock += stockout.quantity

        product.save()

        stockout.delete()

        messages.success(
            request,
            "Barang keluar berhasil dihapus."
        )

        return redirect("stockout_list")

    context = {
        "stockout": stockout,
    }

    return render(
        request,
        "stockout/delete.html",
        context,
    )

#===========================================================================
#REPORTS===================================================================
#===========================================================================
@login_required
def report_stock(request):

    keyword = request.GET.get("q", "")

    category = request.GET.get("category")

    supplier = request.GET.get("supplier")

    status = request.GET.get("status")

    products = Product.objects.select_related(
        "category",
        "supplier"
    ).all()

    if keyword:

        products = products.filter(

            Q(code__icontains=keyword) |
            Q(name__icontains=keyword)

        )

    if category:

        products = products.filter(
            category_id=category
        )

    if supplier:

        products = products.filter(
            supplier_id=supplier
        )

    if status == "low":

        products = products.filter(
            stock__lte=F("minimum_stock")
        )

    elif status == "safe":

        products = products.filter(
            stock__gt=F("minimum_stock")
        )

    context = {

        "products": products,

        "categories": Category.objects.all(),

        "suppliers": Supplier.objects.all(),

        "keyword": keyword,

        "selected_category": category,

        "selected_supplier": supplier,

        "selected_status": status,

    }

    return render(
        request,
        "reports/stock.html",
        context,
    )


@login_required
def report_stockin(request):

    keyword = request.GET.get("q", "")
    supplier = request.GET.get("supplier")
    product = request.GET.get("product")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    stockins = StockIn.objects.select_related(
        "product",
        "supplier"
    ).all()

    if keyword:
        stockins = stockins.filter(
            Q(invoice__icontains=keyword) |
            Q(product__name__icontains=keyword)
        )

    if supplier:
        stockins = stockins.filter(
            supplier_id=supplier
        )

    if product:
        stockins = stockins.filter(
            product_id=product
        )

    if start_date:
        stockins = stockins.filter(
            date__gte=start_date
        )

    if end_date:
        stockins = stockins.filter(
            date__lte=end_date
        )

    context = {

        "stockins": stockins,

        "suppliers": Supplier.objects.all(),

        "products": Product.objects.all(),

        "keyword": keyword,

        "selected_supplier": supplier,

        "selected_product": product,

        "start_date": start_date,

        "end_date": end_date,

    }

    return render(
        request,
        "reports/stockin.html",
        context,
    )

@login_required
def report_stockout(request):

    keyword = request.GET.get("q", "")
    product = request.GET.get("product")
    receiver = request.GET.get("receiver")
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")

    stockouts = StockOut.objects.select_related(
        "product"
    )

    if keyword:
        stockouts = stockouts.filter(
            Q(invoice__icontains=keyword) |
            Q(product__name__icontains=keyword)
        )

    if receiver:
        stockouts = stockouts.filter(
            receiver__icontains=receiver
        )

    if product:
        stockouts = stockouts.filter(
            product_id=product
        )

    if start_date:
        stockouts = stockouts.filter(
            date__gte=start_date
        )

    if end_date:
        stockouts = stockouts.filter(
            date__lte=end_date
        )

    context = {

        "stockouts": stockouts,

        "products": Product.objects.all(),

        "keyword": keyword,

        "receiver": receiver,

        "selected_product": product,

        "start_date": start_date,

        "end_date": end_date,

    }

    return render(
        request,
        "reports/stockout.html",
        context,
    )