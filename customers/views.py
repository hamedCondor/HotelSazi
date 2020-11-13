from django.shortcuts import render, redirect
# from . models import MyUser
# from .forms import MyUserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Adder, CodeUsage, Code
from .forms import AdderForm
from django.utils import timezone
from django.db import models


# tring something new with admin pannel


def daftarcode(request):
    if request.method == 'POST':
        code = request.POST['code']
        get_id = Code.objects.get(code_num=code).id
        if get_id:
            usage = CodeUsage.objects.filter(code = get_id)
            return render(request, 'daftarcode.html', {'usage': usage})
    else:
        return render(request, 'daftarcode.html', {})


# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def addphone(request):
    # if request.method == 'POST':
    #     form = MyUserForm(request.POST or None)
    #
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, '!شماره با موفقیت ثبت شد')
    #         return render(request, 'addphone.html', {})
    # else:
    return render(request, 'addphone.html', {})


def deletephone(request, list_id):
    # muf = MyUser.objects.get(pk=list_id)
    # muf.delete()
    return redirect('phonelist')


def addpresent(request):
    return render(request, 'addpresent.html', {})


def addpurchase(request):
    return render(request, 'addpurchase.html', {})


def phonelist(request):
    return render(request, 'phonelist.html', {})


def presentlist(request):
    return render(request, 'presentlist.html', {})


def purchaselist(request):
    return render(request, 'purchaselist.html', {})


def contactus(request):
    return render(request, 'contactus.html', {})


# def updatephone(request,list_id):
#     if request.method == 'POST':
#         todo_item = MyUser.objects.get(pk=list_id)
#         form = MyUserForm(request.POST or None, instance=todo_item)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Item has been Edited')
#             return redirect('phonelist')
#     else:
#         item = MyUser.objects.get(pk=list_id)
#         return render(request, 'updatephone.html',{'item' : item})

def adders(request):
    if request.method == 'POST':
        form = AdderForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, '!شماره با موفقیت ثبت شد')
            return HttpResponseRedirect('adders')

    else:
        adders_list = Adder.objects.all
        return render(request, 'adders.html', {'adders_list': adders_list})


def deletadder(request, adder_id):
    tobe_deleted = Adder.objects.get(pk=adder_id)
    tobe_deleted.delete()
    return redirect('adders')


def inviters(request):
    if request.method == 'POST':
        form = Inviter(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, '!شماره با موفقیت ثبت شد')
            return HttpResponseRedirect('inviters')

    else:
        inviters_list = Adder.objects.all
        return render(request, 'inviters.html', {'inviters_list': inviters_list})


def deleteinviters(request, inviter_id):
    tobe_deleted = Inviter.objects.get(pk=adder_id)
    tobe_deleted.delete()
    return redirect('inviters')
