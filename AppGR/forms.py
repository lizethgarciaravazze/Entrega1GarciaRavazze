from django import forms


class SombrasForm(forms.Form):
    codigo = forms.IntegerField()
    color = forms.CharField(max_length=100)
    tipo = forms.CharField(max_length=100)

class BaseForm(forms.Form):
    codigo = forms.IntegerField()
    tono = forms.CharField(max_length=100)
    cobertura = forms.CharField(max_length=100)

class BrochasForm(forms.Form):
    numero = forms.IntegerField()
    clase = forms.CharField(max_length=100)