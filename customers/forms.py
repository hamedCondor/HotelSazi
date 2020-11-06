from django import forms
from .models import MyUser

class MyUserForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ["user_phone", "for_date", "for_time", "is_present", "is_purchased", "user_firstname", "user_lastname", "user_address", "national_code"]