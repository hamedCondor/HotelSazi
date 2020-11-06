from django.shortcuts import render, redirect
from . models import MyUser
from .forms import MyUserForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def addphone(request):
    if request.method == 'POST':
        form = MyUserForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, '!شماره با موفقیت ثبت شد')
            return render(request, 'addphone.html', {})
    else:
        return render(request, 'addphone.html', {})


def deletephone(request,list_id):
    muf = MyUser.objects.get(pk=list_id)
    muf.delete()
    return redirect('phonelist')


def addpresent(request):
    return render(request, 'addpresent.html', {})


def addpurchase(request):
    return render(request, 'addpurchase.html', {})


def phonelist(request):
    all_items = MyUser.objects.all
    return render(request, 'phonelist.html', {'all_items' : all_items})


def presentlist(request):
    return render(request, 'presentlist.html', {})


def purchaselist(request):
    return render(request, 'purchaselist.html', {})


def contactus(request):
    return render(request, 'contactus.html',{})
