from django import forms
from .models import ConsultaContacto


class ContactoForm(forms.ModelForm):
    class Meta:
        model = ConsultaContacto
        fields = ["nombre", "email", "mensaje"]
        widgets = {
            "nombre": forms.TextInput(attrs={"placeholder": "Tu nombre"}),
            "email": forms.EmailInput(attrs={"placeholder": "tu@email.com"}),
            "mensaje": forms.Textarea(attrs={"rows": 4, "placeholder": "Escribe tu mensaje"}),
        }
