from django import forms
from .models import *


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'image', 'category', 'tags']

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'product-text-input'

        self.fields['image'].widget.attrs['class'] = 'product-image-input'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description']