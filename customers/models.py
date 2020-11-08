from django.db import models
from django.utils import timezone


# database davatie seminar
class Seminar(models.Model):
    seminar_name = models.CharField(maxlenght=200)
    seminar_date = models.DateField()

    def __str__(self):
        return self.seminar_name

    class Meta:
        ordering = ['seminar_name']


class Sans(models.Model):
    sans = models.CharField(maxlenght=50)
    seminar = models.ForeignKey(Seminar, on_delete=models.CASCADE)

    def __str__(self):
        return self.sans

    class Meta:
        ordering = ['sans']


# class Invited(models.Model):
#     phone_num = models.
class Adder(models.Model):
    first_name = models.CharField(max_lenght=200)
    last_name = models.CharField(max_lenght=200)
    date_of_hired = models.DateField()
    date_of_fired = models.DateField()
    phone_num = models.IntegerField()
    level = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Inviter(models.Model):
    first_name = models.CharField(max_lenght=200)
    last_name = models.CharField(max_lenght=200)
    date_of_hired = models.DateField()
    date_of_fired = models.DateField()
    phone_num = models.IntegerField()

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class Invited(models.Model):
    phone_num = models.IntegerField()
    full_name = models.CharField(max_lenght=200)
    added_datetime = models.DateTimeField(default=timezone.now)
    sans = models.ForeignKey(Sans, on_delete=models.CASCADE)
    added_by = models.ForeignKey(Adder, on_delete=models.CASCADE)
    invited_by = models.ForeignKey(Inviter, on_delete=models.CASCADE)

    def __str__(self):
        return self.phone_num

    class Meta:
        ordering = ['added_datetime']


# database daftar code

class Code(models.Model):
    code_num = models.IntegerField()
    code_prev_num = models.IntegerField(default='0912')

    def __str__(self):
        return self.code_num

    class Meta:
        ordering = ['code_num']


class CodeUsage(models.Model):
    date = models.CharField(max_lenght=50)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)

    def __str__(self):
        return self.date

    class Meta:
        ordering = ['date']
#
# class MyUser(models.Model):
#     user_phone = models.CharField(max_length=11, blank=False)
#     added_datetime = models.DateTimeField(default=timezone.now)
#     added_by = models.CharField(max_length=50, default='Hamed')
#     invited_by = models.CharField(max_length=50, default='Maede')
#     for_date = models.CharField(max_length=11, blank=True, default='NA')
#     for_time = models.CharField(max_length=11, blank=True, default='NA')
#     is_present = models.BooleanField(default=False)
#     is_purchased = models.BooleanField(default=False)
#     user_firstname = models.CharField(max_length=100, blank=True, default='NA')
#     user_lastname = models.CharField(max_length=200, blank=True, default='NA')
#     user_address = models.CharField(max_length=800, blank=True, default='NA')
#     national_code = models.IntegerField(blank=True, default=0)
#
#     def __str__(self):
#         return self.user_phone
