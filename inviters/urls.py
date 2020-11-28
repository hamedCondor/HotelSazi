from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import (
    AllCodeListView,
    InviterListView,
    InviterDetailView,
    InviterCreateView,
    InviterUpdateView,
    InviterDeleteView,
)

urlpatterns = [
    path('', InviterListView.as_view(), name="home"),
    path('daftarcode', views.daftarcode, name="daftarcode"),
    path('allcode', login_required(AllCodeListView.as_view()), name="allcode"),
    path('inviter_new/', InviterCreateView.as_view(), name="inviter_new"),
    path('inviter_detail/<int:pk>/', InviterDetailView.as_view(), name="inviter_detail"),
    path('inviter_detail/<int:pk>/update', InviterUpdateView.as_view(), name="inviter_update"),
    path('inviter_detail/<int:pk>/delete', InviterDeleteView.as_view(), name="inviter_delete"),

    # path('code_feeder', views.code_feeder, name="code_feeder"),
    # path('months_of', views.months_of, name="months_of"),
]
