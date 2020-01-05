from django import forms
from .models import Car, Order, PrivateMsg,CarType

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            "image",
            "car_name",
            "company_name",
            "plate_number",
            "num_of_seats",
            "num_of_bed",
            "cost_par_day",
            "cost_per_week",
            "weekend_cost",
            "content",
        ]
        
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            "car_name",
            "employee_name",
            "cell_no",
            "address",
            "date",
            "to",
        ]
class MessageForm(forms.ModelForm):
    class Meta:
        model = PrivateMsg
        fields = [
            "name",
            "email",
            "message",
        ]
