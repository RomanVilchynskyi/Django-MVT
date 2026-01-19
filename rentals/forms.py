from django import forms
from .models import CarRental

from django import forms
from .models import CarRental

BASE_INPUT_CLASSES = (
    "bg-neutral-secondary-medium border border-default-medium text-heading text-sm "
    "rounded-base focus:ring-brand focus:border-brand block w-full px-3 py-2.5 "
    "shadow-xs placeholder:text-body"
)

class CarRentalForm(forms.ModelForm):
    class Meta:
        model = CarRental
        fields = [
            'car',
            'customer_name',
            'customer_phone',
            'start_date',
            'end_date',
        ]
        widgets = {
            'car': forms.Select(attrs={'class': BASE_INPUT_CLASSES}),
            'customer_name': forms.TextInput(
                attrs={'class': BASE_INPUT_CLASSES, 'placeholder': "Ім'я клієнта"}
            ),
            'customer_phone': forms.TextInput(
                attrs={'class': BASE_INPUT_CLASSES, 'placeholder': '+380...'}
            ),
            'start_date': forms.DateInput(
                attrs={'class': BASE_INPUT_CLASSES, 'type': 'date'}
            ),
            'end_date': forms.DateInput(
                attrs={'class': BASE_INPUT_CLASSES, 'type': 'date'}
            ),
        }

