from django import forms
# from .models import MyUser
from .models import Adder
from django.db import models
from django.utils import timezone


# class MyUserForm(forms.ModelForm):
#     class Meta:
#         model = MyUser
#         fields = ["user_phone", "for_date", "for_time", "is_present", "is_purchased", "user_firstname", "user_lastname", "user_address", "national_code"]


class AdderForm(forms.ModelForm):
    class Meta:
        model = Adder
        fields = ["first_name", "last_name", "date_of_hired", "date_of_fired", "phone_num", "level"]
