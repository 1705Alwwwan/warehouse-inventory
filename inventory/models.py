from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
    
class Supplier(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["company"]

    def __str__(self):
        return self.company
    

class Product(models.Model):
    STATUS = (
        ("active", "Active"),
        ("inactive", "Inactive"),
    )

    code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,
    )

    name = models.CharField(max_length=150)

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="products"
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="products"
    )

    purchase_price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    selling_price = models.DecimalField(
        max_digits=15,
        decimal_places=2
    )

    stock = models.PositiveIntegerField(default=0)
    minimum_stock = models.PositiveIntegerField(default=5)
    rack = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    description = models.TextField(blank=True)

    status = models.CharField(
        max_length=10,
        choices=STATUS,
        default="active"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"
    
    def save(self, *args, **kwargs):
        if not self.code:
            last = Product.objects.order_by("id").last()
            if last:
                number = int(last.code[3:]) + 1
            else:
                number = 1
            self.code = f"BRG{number:04d}"
        super().save(*args, **kwargs)


class StockIn(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="stockin",
    )

    supplier = models.ForeignKey(
        Supplier,
        on_delete=models.PROTECT,
        related_name="stockin",
    )

    quantity = models.PositiveIntegerField()

    price = models.DecimalField(
        max_digits=15,
        decimal_places=2,
    )

    invoice = models.CharField(
        max_length=100,
        blank=True,
    )

    date = models.DateField()

    note = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.product.name} ({self.quantity})"
    
class StockOut(models.Model):

    product = models.ForeignKey(
        Product,
        on_delete=models.PROTECT,
        related_name="stockout",
    )

    quantity = models.PositiveIntegerField()

    invoice = models.CharField(
        max_length=100,
        blank=True,
    )

    receiver = models.CharField(
        max_length=100,
    )

    date = models.DateField()

    note = models.TextField(
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:

        ordering = ["-date"]

    def __str__(self):

        return f"{self.product.name} ({self.quantity})"