from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta:
        model = Visitor
        fields = ['name', 'mobile_no', 'visiting_reason', 'meet_for']
