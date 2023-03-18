from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorsList.as_view(), name='mentors-list'),
    path('<slug:slug>', views.MentorDetail.as_view(), name='mentor-detail'),
    # path('mentorapplication/', views.MentorApplicationForm.as_view(),
    #      name='mentor-application'),
    # path('mentorapplication/thanks/', views.thankPage, name='thank-message'),
]
