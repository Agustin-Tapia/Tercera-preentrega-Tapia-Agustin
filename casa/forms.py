from django import forms
from casa.models import Silla, Sillon, Mesa

class SillaForm(forms.ModelForm):
    class Meta:
        model = Silla
        fields = '__all__'

class SillonForm(forms.ModelForm):
    class Meta:
        model = Sillon
        fields = '__all__'
        
class MesaForm(forms.ModelForm):
    class Meta:
        model = Mesa
        fields = '__all__'