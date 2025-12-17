from django import forms
from .models import Car

BASE_INPUT_CLASSES = (
    "bg-neutral-secondary-medium border border-default-medium text-heading text-sm rounded-base focus:ring-brand focus:border-brand block w-full px-3 py-2.5 shadow-xs placeholder:text-body"
)

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': BASE_INPUT_CLASSES, 'placeholder': 'BMW'}),
            'model': forms.TextInput(attrs={'class': BASE_INPUT_CLASSES, 'placeholder': 'X5'}),
            'year': forms.NumberInput(attrs={'class': BASE_INPUT_CLASSES, 'placeholder': '2022'}),
            'price_per_day': forms.NumberInput(attrs={'class': BASE_INPUT_CLASSES, 'placeholder': '100'}),
            'description': forms.Textarea(attrs={'class': BASE_INPUT_CLASSES, 'rows': 4, 'placeholder': 'Опис автомобіля'}),
            'image': forms.URLInput(attrs={'class': BASE_INPUT_CLASSES, 'placeholder': 'https://...'}),
        }
