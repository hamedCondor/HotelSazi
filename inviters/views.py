from django.contrib.auth.decorators import login_required
from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import datetime
from django.utils import timezone
from django.db import models
from .models import CodeUsage
from django.urls import reverse_lazy
from persiantools.jdatetime import JalaliDate
import jdatetime
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)


@login_required
def daftarcode(request):
    if request.method == 'POST':
        code = request.POST['code']
        try:
            get_id = Code.objects.get(code_num=code).id
        except:
            get_id = None
        if get_id:
            usage = CodeUsage.objects.filter(code=get_id)
            return render(request, 'daftarcode.html', {'usage': usage})

        return render(request, 'daftarcode.html', {})
    else:
        return render(request, 'daftarcode.html', {})


@login_required
def allcode(request):
    getcodes = CodeUsage.objects.all()
    return render(request, 'allcode.html', {'getcodes': getcodes})


class AllCodeListView(ListView):
    model = CodeUsage
    template_name = 'allcode.html'
    context_object_name = 'getcodes'
    ordering = ['code']


class AllCodeFilteredListView(ListView):
    model = CodeUsage
    template_name = 'allcode_filtered.html'
    context_object_name = 'getcodes'
    ordering = ['code']

    def get_queryset(self):
        return CodeUsage.objects.filter(code__code_name=self.kwargs.get('code'))


class CodeUsageCreateView(CreateView):
    model = CodeUsage
    fields = ['code', 'company', 'year_of_use', 'monthof', 'inviter']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, 'گیرنده کد اضافه شد')
        return super().form_valid(form)


@login_required
def home(request):
    return render(request, 'inviters/inviter_list.html', {})


############ inviters AUD list view classes  ##############
class InviterListView(LoginRequiredMixin, ListView):
    model = Inviter


class InviterDetailView(LoginRequiredMixin, DetailView):
    model = Inviter


class InviterCreateView(LoginRequiredMixin, CreateView):
    model = Inviter
    fields = ['first_name', 'last_name', 'date_of_hired', 'phone_num', 'company']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, 'دعوت کننده اضافه شد')
        return super().form_valid(form)


class InviterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inviter
    fields = ['first_name', 'last_name', 'date_of_hired', 'phone_num', 'company']

    def test_func(self):
        form = self.get_object()
        if self.request.user == form.user or self.request.user.is_superuser:
            return True
        return False

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' مشخصات دعوت کننده تغییر یافت')
        form.save()
        return redirect('inviter_list')


class InviterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inviter
    success_url = '/'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


############### Seminar AUD list view classes  ##############


class SeminarListView(LoginRequiredMixin, ListView):
    model = Seminar
    ordering = ['-year', '-month', '-day']
    paginate_by = 2


class SeminarDetailView(LoginRequiredMixin, DetailView):
    model = Seminar


class SeminarCreateView(LoginRequiredMixin, CreateView):
    model = Seminar
    fields = ['year', 'month', 'day', 'company', 'is_vebinar']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, ' سمینار با موفقیت ثبت شد')
        form.save()
        return redirect('seminar_list')


class SeminarUpdateView(LoginRequiredMixin, UpdateView):
    model = Seminar
    fields = ['year', 'month', 'day', 'company', 'is_vebinar']

    def form_valid(self, form):
        messages.add_message(self.request, messages.SUCCESS, ' مشخصات سمینار تغییر یافت')
        form.save()
        return redirect('seminar_list')


class SeminarDeleteView(LoginRequiredMixin, DeleteView):
    model = Seminar
    success_url = reverse_lazy('seminar_list')


################# Penalty AUD list view classes #########################

class PenaltyListView(LoginRequiredMixin, ListView):
    model = Penalty
    ordering = ['-date']
    paginate_by = 10

    def get_queryset(self):
        inviter_id = get_object_or_404(Inviter, id=self.kwargs.get('inviter_id'))
        return Penalty.objects.filter(inviter=inviter_id).order_by('-date')


class PenaltyDetailView(LoginRequiredMixin, DetailView):
    model = Penalty


class PenaltyCreateView(LoginRequiredMixin, CreateView):
    model = Reward
    fields = ['inviter', 'date', 'amount', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' جریمه با موفقیت ثبت شد')
        return form


class PenaltyIDCreateView(LoginRequiredMixin, CreateView):
    model = Penalty
    fields = ['date', 'amount', 'description']

    def form_valid(self, form):
        inviter_id = self.kwargs['inviter_id']
        inviter = Inviter.objects.get(pk=inviter_id)
        form.instance.inviter = inviter
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' جریمه با موفقیت ثبت شد')
        return super().form_valid(form)


class PenaltyUpdateView(LoginRequiredMixin, UpdateView):
    model = Penalty
    fields = ['date', 'amount', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' جریمه با موفقیت بروزرسانی شد')
        form.save()
        return redirect('inviter_list')


class PenaltyDeleteView(LoginRequiredMixin, DeleteView):
    model = Penalty
    success_url = reverse_lazy('inviter_list')


################# Reward AUD list view classes #########################

class RewardListView(LoginRequiredMixin, ListView):
    model = Reward
    ordering = ['-date']
    paginate_by = 10

    def get_queryset(self):
        inviter_id = get_object_or_404(Inviter, id=self.kwargs.get('inviter_id'))
        return Reward.objects.filter(inviter=inviter_id).order_by('-date')


class RewardDetailView(LoginRequiredMixin, DetailView):
    model = Reward


class RewardCreateView(LoginRequiredMixin, CreateView):
    model = Reward
    fields = ['inviter', 'date', 'amount', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' پاداش با موفقیت ثبت شد')
        return form


class RewardIDCreateView(LoginRequiredMixin, CreateView):
    model = Reward
    fields = ['date', 'amount', 'description']

    def form_valid(self, form):
        inviter_id = self.kwargs['inviter_id']
        inviter = Inviter.objects.get(pk=inviter_id)
        form.instance.inviter = inviter
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' پاداش با موفقیت ثبت شد')
        return super().form_valid(form)


class RewardUpdateView(LoginRequiredMixin, UpdateView):
    model = Reward
    fields = ['date', 'amount', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' پاداش با موفقیت بروزرسانی شد')
        form.save()
        return redirect('inviter_list')


class RewardDeleteView(LoginRequiredMixin, DeleteView):
    model = Reward
    success_url = reverse_lazy('inviter_list')


################# HourlyOffTime AUD list view classes #########################

class HourlyOffTimeListView(LoginRequiredMixin, ListView):
    model = HourlyOffTime
    ordering = ['-date']
    paginate_by = 10

    def get_queryset(self):
        inviter_id = get_object_or_404(Inviter, id=self.kwargs.get('inviter_id'))
        return HourlyOffTime.objects.filter(inviter=inviter_id).order_by('-date')


class HourlyOffTimeDetailView(LoginRequiredMixin, DetailView):
    model = HourlyOffTime


class HourlyOffTimeCreateView(LoginRequiredMixin, CreateView):
    model = HourlyOffTime
    fields = ['inviter', 'date', 'start_time', 'end_time', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' مرخصی ساعتی با موفقیت ثبت شد')
        return super().form_valid(form)


class HourlyOffTimeIDCreateView(LoginRequiredMixin, CreateView):
    model = HourlyOffTime
    fields = ['date', 'start_time', 'end_time', 'description']

    def form_valid(self, form):
        inviter_id = self.kwargs['inviter_id']
        inviter = Inviter.objects.get(pk=inviter_id)
        form.instance.inviter = inviter
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' مرخصی ساعتی با موفقیت ثبت شد')
        return super().form_valid(form)


class HourlyOffTimeUpdateView(LoginRequiredMixin, UpdateView):
    model = HourlyOffTime
    fields = ['date', 'amount', 'description']

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(self.request, messages.SUCCESS, ' مرخصی ساعتی با موفقیت بروزرسانی شد')
        form.save()
        return redirect('inviter_list')


class HourlyOffTimeDeleteView(LoginRequiredMixin, DeleteView):
    model = HourlyOffTime
    success_url = reverse_lazy('inviter_list')

# ############ this view force fed db codes with prev number of 0912 and range of nubers from 000 to 999
# def code_feeder(request):
#     counter = 10
#     my_code_list = ["000", "001", "002", "003", "004", "005", "006", "007", "008", "009"]
#
#     while counter < 1000:
#         if counter < 100:
#             my_code_list.append(f'0{counter}')
#             counter += 1
#         else:
#             my_code_list.append(f'{counter}')
#             counter += 1
#     for code in my_code_list:
#         code_first = code[0]
#         feeder = CodeForm({
#             'code_num': code,
#             'code_prev_num': '0912',
#             'code_name': code_first
#         })
#         feeder.save()
#     return render(request, 'inviter_list.html', {})
#
#
#
# #########this code force fed db 12 months of year , farvardin = 1 ,,,, esfand = 12
# def months_of(request):
#     months_name = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور", "مهر", "آبان", "آذر", "دی", "بهمن",
#                    "اسفند"]
#     months_number = 1
#     for month in months_name:
#         feeder = MonthForm({
#             'month_number': months_number,
#             'month_name': month
#         })
#         feeder.save()
#         months_number += 1
#     return render(request, '/', {})
