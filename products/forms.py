from django import forms

from products.models import Product


class ProductModelForm(forms.ModelForm):
    """Form definition for Product."""

    class Meta:
        """Meta definition for Productform."""

        model = Product
        fields = '__all__'
