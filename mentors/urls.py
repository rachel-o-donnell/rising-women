from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorsList.as_view(), name='mentorslist'),
    path('<slug:slug>', views.MentorDetail.as_view(), name='mentordetail'),
]
