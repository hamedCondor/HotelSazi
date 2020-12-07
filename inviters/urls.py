from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import (
    AllCodeListView,
    AllCodeFilteredListView,
    ##### inviters views #####
    InviterListView,
    InviterDetailView,
    InviterCreateView,
    InviterUpdateView,
    InviterDeleteView,
    ##### Seminar views #####
    SeminarListView,
    SeminarDetailView,
    SeminarCreateView,
    SeminarUpdateView,
    SeminarDeleteView,
    ####### penalty ######
    PenaltyListView,
    PenaltyDetailView,
    PenaltyCreateView,
    PenaltyUpdateView,
    PenaltyDeleteView,
)

urlpatterns = [
    ### Daftar code Urls ###
    path('daftarcode/', views.daftarcode, name="daftarcode"),
    path('allcode/', login_required(AllCodeListView.as_view()), name="allcode"),
    path('allcode_filtered/<code>/', login_required(AllCodeFilteredListView.as_view()), name="allcode_filtered"),

    ### Inviters URls ###
    path('', InviterListView.as_view(), name="inviter_list"),
    path('inviter_new/', InviterCreateView.as_view(), name="inviter_new"),
    path('inviter_detail/<int:pk>/', InviterDetailView.as_view(), name="inviter_detail"),
    path('inviter_detail/<int:pk>/update/', InviterUpdateView.as_view(), name="inviter_update"),
    path('inviter_detail/<int:pk>/delete/', InviterDeleteView.as_view(), name="inviter_delete"),
    ### Seminars Urls ###
    path('seminar_list/', SeminarListView.as_view(), name="seminar_list"),
    path('seminar_form/', SeminarCreateView.as_view(), name="seminar_new"),
    path('seminar_form/<int:pk>/update/', SeminarUpdateView.as_view(), name="seminar_update"),
    path('seminar_delete/<int:pk>/delete/', SeminarDeleteView.as_view(), name="seminar_delete"),
    ### penalty ###
    path('penalty_form/', PenaltyCreateView.as_view(), name="penalty_new"),
    path('penalty_list/<int:inviter_id>/', PenaltyListView.as_view(), name="penalty_list"),
    path('penalty_detail/<int:pk>/', PenaltyDetailView.as_view(), name="penalty_detail"),
    path('penalty_form/<int:pk>/update/', PenaltyUpdateView.as_view(), name="penalty_update"),
    path('penalty_delete/<int:pk>/delete/', PenaltyDeleteView.as_view(), name="penalty_delete"),





    # path('code_feeder', views.code_feeder, name="code_feeder"),
    # path('months_of', views.months_of, name="months_of"),
]

