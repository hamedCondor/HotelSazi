from django.utils import timezone
from django.db import models
import datetime


class Company(models.Model):
    company_name = models.CharField(max_length=400)

    def __str__(self):
        return self.company_name


class Code(models.Model):
    code_num = models.CharField(max_length=3)
    code_prev_num = models.IntegerField(default='0912')

    def __str__(self):
        return '0%s | %s' % (self.code_prev_num, self.code_num)

    class Meta:
        ordering = ['code_num']


class MonthOf(models.Model):
    month_number = models.IntegerField()
    month_name = models.CharField(default='فروردین', max_length=20)

    def __str__(self):
        return self.month_name

    class Meta:
        ordering = ['month_number']


class Inviter(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_hired = models.DateTimeField(default=timezone.now)
    phone_num = models.CharField(max_length=11)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)


class CodeUsage(models.Model):
    year_of_use = models.CharField(max_length=4, default=1399)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    monthof = models.ForeignKey(MonthOf, on_delete=models.CASCADE)

    def __str__(self):
        return self.year_of_use


class Sells(models.Model):
    weeks_of = models.IntegerField()
    monthof = models.ForeignKey(MonthOf, on_delete=models.CASCADE)
    year_of = models.IntegerField(default=1400)
    price_of_sell = models.CharField(max_length=30)
    extra_detail = models.TextField(null=True, blank=True)
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} فروش'


class HourlyOffTime(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'  مرخصی ساعتی :{self.inviter.first_name}  {self.inviter.last_name}  {self.start_time}  تا {self.end_time} '


class DailyOffTime(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    start_date = models.DateField(default=datetime.date.today)
    end_date = models.DateField()
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'  مرخصی روزانه :{self.inviter.first_name}  {self.inviter.last_name}  {self.start_date}  تا {self.end_date} '


class Penalty(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    amount = models.CharField(max_length=20)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} جریمه '


class Reward(models.Model):
    inviter = models.ForeignKey(Inviter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    amount = models.CharField(max_length=20)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.inviter.first_name} {self.inviter.last_name} پاداش '
