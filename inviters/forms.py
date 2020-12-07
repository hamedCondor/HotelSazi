from django import forms
# from .models import MyUser
from .models import Inviter, Code, MonthOf, Penalty
from django.db import models
from django.utils import timezone


class InvitersForm(forms.ModelForm):
    class Meta:
        model = Inviter
        fields = ["first_name", "last_name", "date_of_hired", "phone_num"]


class PenaltyForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        inviter = kwargs.pop('inviter', None)  # pop the 'user' from kwargs dictionary
        super(PenaltyForm, self).__init__(*args, **kwargs)
        self.fields['penalty'] = forms.ModelChoiceField(queryset=Penalty.objects.filter(inviter=inviter))


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ["code_num", "code_prev_num", "code_name"]


class MonthForm(forms.ModelForm):
    class Meta:
        model = MonthOf
        fields = ["month_name", "month_number"]
