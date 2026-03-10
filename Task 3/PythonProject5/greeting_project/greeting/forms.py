from django import forms
from .models import UserName


class NameForm(forms.ModelForm):
    class Meta:
        model = UserName
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваше имя',
                'autocomplete': 'off'
            })
        }
        labels = {
            'name': 'Ваше имя'
        }

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name or name.strip() == '':
            raise forms.ValidationError('Поле имени не может быть пустым')
        return name.strip()