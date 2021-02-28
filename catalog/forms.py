from django import forms

from .models import Category

class ProductFilterForm(forms.Form):
    q = forms.CharField(label='Search', required=False)
    category_id = forms.ModelMultipleChoiceField(
        label='Category',
        queryset=Category.objects.all(),
        queryset=forms.CheckboxSelectMultiple,
        required=False
    )
    max_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)
    min_price = forms.DecimalField(decimal_places=2, max_digits=12, required=False)

