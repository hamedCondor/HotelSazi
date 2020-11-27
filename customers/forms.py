from django import forms
# from .models import MyUser
from .models import Inviter,Code
from django.db import models
from django.utils import timezone


class InvitersForm(forms.ModelForm):
    class Meta:
        model = Inviter
        fields = ["first_name", "last_name", "date_of_hired", "phone_num"]


class CodeForm(forms.ModelForm):
    class Meta:
        model = Code
        fields = ["code_num", "code_prev_num"]
