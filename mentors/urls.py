from django.urls import path
from . import views

urlpatterns = [
    path('', views.MentorsList.as_view(), name='mentors-list'),
    path('<slug:mentor_slug>/', views.MentorDetail.as_view(),
         name='mentor-detail'),
    path('mentor-search/', views.mentor_search, name='mentor_search'),
]
