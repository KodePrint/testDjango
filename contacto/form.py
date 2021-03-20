from django import forms
from django.core.exceptions import ValidationError

from .models import Contact

class FormContatc(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget.attrs['required'] = False
        self.fields['user'].widget.attrs['hidden'] = True

    class Meta:
        model = Contact
        fields = 'name', 'telephone', 'email', 'user',
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Name',
                'class': 'form-control'
            }),
            'telephone': forms.TextInput(attrs={
                'placeholder': 'Telephone',
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Email',
                'class': 'form-control'
            })
        }
        labels = {'user':''}

    # Metodo que validara los campos y lanzara un error si ambos estan vacios
    def clean(self):
        cleaned_data = super(FormContatc, self).clean()
        email = cleaned_data.get("email")
        telephone = cleaned_data.get("telephone")
        if email==None and telephone==None:
            raise ValidationError("You must enter one of these fields: telephone / email")
