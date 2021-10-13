from .models import Provinces
from django import forms
import datetime

class ProvincesForm(forms.ModelForm):
    ## change the widget of the date field.

    def __init__(self, *args, **kwargs):
        super(ProvincesForm, self).__init__(*args, **kwargs)
        ## add a "form-control" class to each form input
        ## for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = Provinces
        fields = ("__all__")