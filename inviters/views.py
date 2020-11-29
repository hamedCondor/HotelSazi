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
from django.urls import reverse_lazy
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


@login_required
def home(request):
    return render(request, 'inviter_list.html', {})


############ inviters AUD ##############
class InviterListView(LoginRequiredMixin, ListView):
    model = Inviter
    template_name = 'inviter_list.html'


class InviterDetailView(LoginRequiredMixin, DetailView):
    model = Inviter
    template_name = 'inviter_detail.html'


class InviterCreateView(LoginRequiredMixin, CreateView):
    model = Inviter
    template_name = 'inviter_form.html'
    fields = ['first_name', 'last_name', 'date_of_hired', 'phone_num', 'company']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class InviterUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Inviter
    template_name = 'inviter_form.html'
    fields = ['first_name', 'last_name', 'date_of_hired', 'phone_num', 'company']

    def test_func(self):
        form = self.get_object()
        if self.request.user == form.user or self.request.user.is_superuser:
            return True
        return False


class InviterDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Inviter
    template_name = 'inviter_confirm_delete.html'
    success_url = '/'

    def test_func(self):
        if self.request.user.is_superuser:
            return True
        return False


############### Seminar AUD ##############


class SeminarListView(LoginRequiredMixin, ListView):
    model = Seminar
    template_name = 'seminar_list.html'
    ordering = ['-year', '-month', '-day']
    paginate_by = 10


class SeminarDetailView(LoginRequiredMixin, DetailView):
    model = Seminar
    template_name = 'seminar_detail.html'


class SeminarCreateView(LoginRequiredMixin, CreateView):
    model = Seminar
    template_name = 'seminar_form.html'
    fields = ['year', 'month', 'day', 'company', 'is_vebinar']


class SeminarUpdateView(LoginRequiredMixin, UpdateView):
    model = Seminar
    template_name = 'seminar_form.html'
    fields = ['year', 'month', 'day', 'company', 'is_vebinar']


class SeminarDeleteView(LoginRequiredMixin, DeleteView):
    model = Seminar
    template_name = 'seminar_confirm_delete.html'
    success_url = reverse_lazy('seminar_list')


class PenaltyCreateView(LoginRequiredMixin, CreateView):
    model = Penalty
    template_name = 'penalty_form.html'
    fields = ['inviter', 'date', 'amount', 'description']

# ############code feeder
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
#         feeder = CodeForm({
#             'code_num': code,
#             'code_prev_num': '0912'
#         })
#         feeder.save()
#     return render(request, 'inviter_list.html', {})
#
# #########months feeder
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
#     return render(request, 'inviter_list.html', {})
