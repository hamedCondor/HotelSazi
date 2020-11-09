from django.shortcuts import render, redirect
# from . models import MyUser
# from .forms import MyUserForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Adder
from .forms import AdderForm
from django.utils import timezone
from django.db import models


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
