from django.db import models
from django.utils import timezone


class MyUser(models.Model):
    user_phone = models.CharField(max_length=11, blank=False)
    added_datetime = models.DateTimeField(default=timezone.now)
    added_by = models.CharField(max_length=50, default='Hamed')
    invited_by = models.CharField(max_length=50, default='Maede')
    for_date = models.CharField(max_length=11, blank=True, default='NA')
    for_time = models.CharField(max_length=11, blank=True, default='NA')
    is_present = models.BooleanField(default=False)
    is_purchased = models.BooleanField(default=False)
    user_firstname = models.CharField(max_length=100, blank=True, default='NA')
    user_lastname = models.CharField(max_length=200, blank=True, default='NA')
    user_address = models.CharField(max_length=800, blank=True, default='NA')
    national_code = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.user_phone
