from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import AllCodeListView,HomeListView,HomeDetailView

urlpatterns = [
    path('', login_required(HomeListView.as_view()), name="home"),
    path('inviter_detail/<int:pk>/', login_required(HomeDetailView.as_view()), name="inviter_detail"),
    path('daftarcode', views.daftarcode, name="daftarcode"),
    path('allcode', login_required(AllCodeListView.as_view()), name="allcode"),

    # path('code_feeder', views.code_feeder, name="code_feeder"),
]
