from django.forms import ModelForm
from .models import Order

class OrderForm(ModelForm):
    class meta:
        model= Order
        fields='__all__'