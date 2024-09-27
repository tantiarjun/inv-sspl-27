# inventory/forms.py

from django import forms
from .models import Item
from .models import Supplier

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'category', 'unit_price','image']
        
# Optional: Add widgets for form customization
    image = forms.ImageField(required=False) 
    
    
class SupplierForm(forms.ModelForm):
    class Meta:
        model=Supplier
        fields=['supplier_name','phone_no','address']