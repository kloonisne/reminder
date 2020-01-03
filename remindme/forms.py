from django import forms
from .models import tbl_rmndr


class ReminderForm(forms.ModelForm):

    class Meta:
        model = tbl_rmndr
        fields = ('reminder', 'rmdate')
        labels = {
            'reminder':'Full Name',
            'rmdate':'enter date'
        }
