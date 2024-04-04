from django import forms
from .models import Hostel


class HostelForm(forms.ModelForm):
    class Meta:
        model = Hostel
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "phone": forms.NumberInput(),
            "email": forms.TextInput(attrs={"class": "form-control"}),
            "room": forms.RadioSelect(),
            "arrival_date": forms.DateInput(attrs={"type": "date"}),
            "leave_date": forms.DateInput(attrs={"type": "date"})
        }
        

