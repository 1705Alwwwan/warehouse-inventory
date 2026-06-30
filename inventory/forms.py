from django import forms
from .models import Category, Supplier, Product,StockIn, StockOut


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

        fields = [
            "name",
            "description",
        ]

        widgets = {
            "name": forms.TextInput(
                attrs={
                    "class": "form-control"
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4
                }
            ),
        }

class SupplierForm(forms.ModelForm):
    class Meta:

        model = Supplier

        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class":"form-control"}),
            "company": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "phone": forms.TextInput(attrs={"class":"form-control"}),
            "address": forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            }),

            "city": forms.TextInput(attrs={"class":"form-control"}),

        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = [
            "code",
            "created_at",
            "updated_at",
        ]

        widgets = {
                    "name": forms.TextInput(attrs={
                        "class":"form-control"
                    }),

                    "category": forms.Select(attrs={
                        "class":"form-select"
                    }),

                    "supplier": forms.Select(attrs={
                        "class":"form-select"
                    }),

                    "purchase_price": forms.NumberInput(attrs={
                        "class":"form-control"
                    }),

                    "selling_price": forms.NumberInput(attrs={
                        "class":"form-control"
                    }),

                    "stock": forms.NumberInput(attrs={
                        "class":"form-control"
                    }),

                    "minimum_stock": forms.NumberInput(attrs={
                        "class":"form-control"
                    }),

                    "rack": forms.TextInput(attrs={
                        "class":"form-control"
                    }),

                    "description": forms.Textarea(attrs={
                        "class":"form-control",
                        "rows":4
                    }),

                    "status": forms.Select(attrs={
                        "class":"form-select"
                    }),

                }
        
class StockInForm(forms.ModelForm):

    class Meta:

        model = StockIn

        fields = "__all__"

        widgets = {

            "product": forms.Select(attrs={
                "class":"form-select"
            }),

            "supplier": forms.Select(attrs={
                "class":"form-select"
            }),

            "quantity": forms.NumberInput(attrs={
                "class":"form-control"
            }),

            "price": forms.NumberInput(attrs={
                "class":"form-control"
            }),

            "invoice": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "date": forms.DateInput(attrs={
                "class":"form-control",
                "type":"date"
            }),

            "note": forms.Textarea(attrs={
                "class":"form-control",
                "rows":3
            }),

        }

class StockOutForm(forms.ModelForm):

    class Meta:

        model = StockOut

        fields = "__all__"

        widgets = {

            "product": forms.Select(attrs={
                "class":"form-select"
            }),

            "quantity": forms.NumberInput(attrs={
                "class":"form-control"
            }),

            "invoice": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "receiver": forms.TextInput(attrs={
                "class":"form-control"
            }),

            "date": forms.DateInput(attrs={
                "class":"form-control",
                "type":"date"
            }),

            "note": forms.Textarea(attrs={
                "class":"form-control",
                "rows":4
            }),

        }