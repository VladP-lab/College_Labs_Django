from django import forms
from .models import Rating

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['score']
        labels = {'score': 'Ваша оцінка'}
        widgets = {
            'score': forms.Select(attrs={'style': 'padding: 5px; border-radius: 5px;'})
        }