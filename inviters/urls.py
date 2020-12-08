from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from . import views
from .views import (
    AllCodeListView,
    AllCodeFilteredListView,
    CodeUsageCreateView,
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
    PenaltyIDCreateView,
    ####### reward ######
    RewardListView,
    RewardDetailView,
    RewardCreateView,
    RewardUpdateView,
    RewardDeleteView,
    RewardIDCreateView,
####### reward ######
    HourlyOffTimeListView,
    HourlyOffTimeDetailView,
    HourlyOffTimeCreateView,
    HourlyOffTimeUpdateView,
    HourlyOffTimeDeleteView,
    HourlyOffTimeIDCreateView,
)

urlpatterns = [
    ### Daftar code Urls ###
    path('daftarcode/', views.daftarcode, name="daftarcode"),
    path('allcode/', login_required(AllCodeListView.as_view()), name="allcode"),
    path('allcode_filtered/<code>/', login_required(AllCodeFilteredListView.as_view()), name="allcode_filtered"),
    path('codeusage', login_required(CodeUsageCreateView.as_view()), name='codeusage_new'),
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
    path('penalty_form/<int:inviter_id>/', PenaltyIDCreateView.as_view(), name="penalty_new_id"),
    path('penalty_list/<int:inviter_id>/', PenaltyListView.as_view(), name="penalty_list"),
    path('penalty_detail/<int:pk>/', PenaltyDetailView.as_view(), name="penalty_detail"),
    path('penalty_form/<int:pk>/update/', PenaltyUpdateView.as_view(), name="penalty_update"),
    path('penalty_delete/<int:pk>/delete/', PenaltyDeleteView.as_view(), name="penalty_delete"),
    ### reward ###
    path('reward_form/', RewardCreateView.as_view(), name="reward_new"),
    path('reward_form/<int:inviter_id>/', RewardIDCreateView.as_view(), name="reward_new_id"),
    path('reward_list/<int:inviter_id>/', RewardListView.as_view(), name="reward_list"),
    path('reward_detail/<int:pk>/', RewardDetailView.as_view(), name="reward_detail"),
    path('reward_form/<int:pk>/update/', RewardUpdateView.as_view(), name="reward_update"),
    path('reward_delete/<int:pk>/delete/', RewardDeleteView.as_view(), name="reward_delete"),
    ### hourlyofftime ###
    path('hourlyofftime_form/', HourlyOffTimeCreateView.as_view(), name="hourlyofftime_new"),
    path('hourlyofftime_form/<int:inviter_id>/', HourlyOffTimeIDCreateView.as_view(), name="hourlyofftime_new_id"),
    path('hourlyofftime_list/<int:inviter_id>/', HourlyOffTimeListView.as_view(), name="hourlyofftime_list"),
    path('hourlyofftime_detail/<int:pk>/', HourlyOffTimeDetailView.as_view(), name="hourlyofftime_detail"),
    path('hourlyofftime_form/<int:pk>/update/', HourlyOffTimeUpdateView.as_view(), name="hourlyofftime_update"),
    path('hourlyofftime_delete/<int:pk>/delete/', HourlyOffTimeDeleteView.as_view(), name="hourlyofftime_delete"),
    # path('code_feeder', views.code_feeder, name="code_feeder"),
    # path('months_of', views.months_of, name="months_of"),
]
