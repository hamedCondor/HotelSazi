from django.utils import timezone
from django.db import models
import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Company(models.Model):
    company_name = models.CharField(max_length=400, unique=True)

    def __str__(self):
        return self.company_name


class Code(models.Model):
    code_num = models.CharField(max_length=3)
    code_prev_num = models.IntegerField(default='0912')
    code_name = models.CharField(max_length=1)

    def __str__(self):
        return '0%s | %s' % (self.code_prev_num, self.code_num)

    class Meta:
        ordering = ['code_num']
        unique_together = ["code_num", "code_prev_num"]


class MonthOf(models.Model):
    month_number = models.IntegerField(unique=True)
    month_name = models.CharField(default='فروردین', max_length=20, unique=True)

    def __str__(self):
        return self.month_name

    class Meta:
        ordering = ['month_number']


class Seminar(models.Model):
    year = models.IntegerField(default=1400)
    month = models.ForeignKey(MonthOf, on_delete=models.PROTECT)
    day = models.IntegerField(default=15)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    is_vebinar = models.BooleanField(default=False)

    def __str__(self):
        return "سمینار %s %s/%s/%s " % (self.company, self.year, self.month, self.day)

    def get_absolute_url(self):
        return reverse('seminar_list')

    class Meta:
        unique_together = ['year', 'month', 'day', 'company', 'is_vebinar']


class Inviter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_hired = models.DateTimeField(default=timezone.now)
    date_of_fired = models.DateTimeField(null=True, blank=True)
    date_of_start_esurance = models.DateTimeField(null=True, blank=True)
    date_of_end_esurance = models.DateTimeField(null=True, blank=True)
    is_ensured = models.BooleanField(default=False)
    is_fired = models.BooleanField(default=False)
    phone_num = models.CharField(max_length=11, unique=True)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse('inviter_new')


class CodeUsage(models.Model):
    code = models.ForeignKey(Code, on_delete=models.PROTECT)
    year_of_use = models.IntegerField(default=1400)
    monthof = models.ForeignKey(MonthOf, on_delete=models.PROTECT)
    inviter = models.ForeignKey(Inviter, on_delete=models.PROTECT)
    company = models.ForeignKey(Company, on_delete=models.PROTECT)

    def __str__(self):
        return 'code'

    class Meta:
        unique_together = ['code', 'year_of_use', 'monthof', 'inviter', 'company']

    def get_absolute_url(self):
        return reverse('codeusage_new')


class TahatorSells(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.PROTECT)
    price_of_sell = models.CharField(max_length=30)
    extra_detail = models.TextField(null=True, blank=True)
    inviter = models.ForeignKey(Inviter, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} فروش'


class HotelSaziSells(models.Model):
    seminar = models.ForeignKey(Seminar, on_delete=models.PROTECT)
    inviter = models.ForeignKey(Inviter, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} فروش'


class HourlyOffTime(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'  مرخصی ساعتی :{self.inviter.first_name}  {self.inviter.last_name}  {self.start_time}  تا {self.end_time} '

    class Meta:
        unique_together = ['inviter', 'date', 'start_time', 'end_time', 'description']

    def get_absolute_url(self):
        return reverse('inviter_list')

class DailyOffTime(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'  مرخصی روزانه :{self.inviter.first_name}  {self.inviter.last_name}  {self.start_date}  تا {self.end_date} '

    class Meta:
        unique_together = ['inviter', 'start_date', 'end_date', 'description']

    def get_absolute_url(self):
        return reverse('inviter_list')


class Penalty(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    amount = models.CharField(max_length=20)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} جریمه '

    def get_absolute_url(self):
        return reverse('inviter_list')


class Reward(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    amount = models.CharField(max_length=20)
    description = models.TextField(null=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} پاداش '

    def get_absolute_url(self):
        return reverse('inviter_list')
