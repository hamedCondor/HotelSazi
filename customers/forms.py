from django import forms
# from .models import MyUser
from .models import *
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


class InvitersForm(forms.ModelForm):
    class Meta:
        model = Inviter
        fields = ["first_name", "last_name", "date_of_hired", "date_of_fired", "phone_num"]

class InvitedForm(forms.ModelForm):
    class Meta:
        model = Invited
        fields = ["phone_num","full_name","added_datetime","sans","added_by","invited_by"]


class SeminarForm(forms.ModelForm):
    class Meta:
        model = Seminar
        fields = ["seminar_name","seminar_date"]


class SansForm(forms.ModelForm):
    class Meta:
        model = Sans
        fields = ["sans","seminar"]