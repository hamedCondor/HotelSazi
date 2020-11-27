from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
import datetime
from django.utils import timezone
from django.db import models
from django.views.generic import ListView,DetailView


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
    return render(request, 'home.html', {})

class HomeListView(ListView):
    model = Inviter
    template_name = 'home.html'

class HomeDetailView(DetailView):
    model = Inviter
    template_name = 'inviter_detail.html'

#
# def addphone(request):
#     # if request.method == 'POST':
#     #     form = MyUserForm(request.POST or None)
#     #
#     #     if form.is_valid():
#     #         form.save()
#     #         messages.success(request, '!شماره با موفقیت ثبت شد')
#     #         return render(request, 'addphone.html', {})
#     # else:
#     return render(request, 'addphone.html', {})
#
#
# def deletephone(request, list_id):
#     # muf = MyUser.objects.get(pk=list_id)
#     # muf.delete()
#     return redirect('phonelist')
#
#
# def addpresent(request):
#     return render(request, 'addpresent.html', {})
#
#
# def addpurchase(request):
#     return render(request, 'addpurchase.html', {})
#
#
# def phonelist(request):
#     return render(request, 'phonelist.html', {})
#
#
# def presentlist(request):
#     return render(request, 'presentlist.html', {})
#
#
# def purchaselist(request):
#     return render(request, 'purchaselist.html', {})
#
#
# def contactus(request):
#     return render(request, 'contactus.html', {})
#
#
# # def updatephone(request,list_id):
# #     if request.method == 'POST':
# #         todo_item = MyUser.objects.get(pk=list_id)
# #         form = MyUserForm(request.POST or None, instance=todo_item)
# #         if form.is_valid():
# #             form.save()
# #             messages.success(request, 'Item has been Edited')
# #             return redirect('phonelist')
# #     else:
# #         item = MyUser.objects.get(pk=list_id)
# #         return render(request, 'updatephone.html',{'item' : item})
#
# def adders(request):
#     if request.method == 'POST':
#         form = AdderForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '!شماره با موفقیت ثبت شد')
#             return HttpResponseRedirect('adders')
#
#     else:
#         adders_list = Adder.objects.all
#         return render(request, 'adders.html', {'adders_list': adders_list})
#
#
# def deletadder(request, adder_id):
#     tobe_deleted = Adder.objects.get(pk=adder_id)
#     tobe_deleted.delete()
#     return redirect('adders')
#
#
# def inviters(request):
#     if request.method == 'POST':
#         form = InvitersForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '!شماره با موفقیت ثبت شد')
#             return HttpResponseRedirect('inviters')
#     else:
#         inviters_list = Inviter.objects.all
#         return render(request, 'inviters.html', {'inviters_list': inviters_list})
#
#
# def deleteinviters(request, inviter_id):
#     tobe_deleted = Inviter.objects.get(pk=inviter_id)
#     tobe_deleted.delete()
#     return redirect('inviters')
#
#
# def addguesst(request):
#     adders_list = Adder.objects.all()
#     inviter_list = Inviter.objects.all()
#     return render(request, 'addguesst.html', {'adders_list': adders_list, 'inviter_list': inviter_list})
#
#
# def addseminardate(request):
#     if request.method == 'POST':
#         form = SeminarForm(request.POST or None)
#         if form.is_valid():
#             form.save()
#             messages.success(request, '!شماره با موفقیت ثبت شد')
#             return HttpResponseRedirect('addseminardate')
#     else:
#         return render(request, 'addseminardate.html', {})
#
#
# # https://www.code-learner.com/django-class-based-add-delete-update-and-select-example/
# def addsans(request):
#     if request.method == 'POST':
#
#         form = SansForm(request.POST or None)
#         seminars = Seminar.objects.get(pk=form.seminar)
#         form.seminar = seminars.id
#         if form.is_valid():
#             form.save()
#             messages.success(request, '!شماره با موفقیت ثبت شد')
#             return HttpResponseRedirect('addsans')
#     else:
#         seminar_list = Seminar.objects.all()
#         return render(request, 'addsans.html', {'seminar_list': seminar_list})

# code feeder
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
#     return render(request, 'home.html', {})
