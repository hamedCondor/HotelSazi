from django.contrib import admin
from django.urls import path
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.home, name="home"),
    path('addphone.html', views.addphone, name="addphone"),
    path('addpresent.html', views.addpresent, name="addpresent"),
    path('addpurchase.html', views.addpurchase, name="addpurchase"),
    path('phonelist.html', views.phonelist, name="phonelist"),
    path('presentlist.html', views.presentlist, name="presentlist"),
    path('purchaselist.html', views.purchaselist, name="purchaselist"),
    path('contactus.html', views.contactus, name="contactus"),
    path('deletephone', views.deletephone, name='deletephone'),
    # path('updatephone', views.updatephone, name='updatephone'),
    path('adders', views.adders, name="adders")
]