from django import forms
from . models import Confession

class ConfessionForm(forms.ModelForm):
    class Meta:
        '''
            in the Meta class, here we specify what database table that this
            "form" will act upon. In this case, it will perform CREATE
            operations for Confession (table)
            
        '''
        model = Confession
        fields = ['content']
