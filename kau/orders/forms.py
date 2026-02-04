from django import forms


class CheckoutForm(forms.Form):
    nombre = forms.CharField(max_length=120)
    email = forms.EmailField()
