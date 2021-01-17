from django import forms
from django.core.exceptions import ValidationError

from .models import Etudiant, Chambre
from phonenumber_field.formfields import PhoneNumberField

class EtudiantForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = '__all__'

class Chambreform(forms.ModelForm):
    class Meta:
        model = Chambre
        fields = '__all__'
    

    def clean_batnumber(self):
        batnumber = self.cleaned_data.get('batnumber')
        if len(batnumber)<4:
            raise ValidationError('the batnumber is too short')
        
        return batnumber