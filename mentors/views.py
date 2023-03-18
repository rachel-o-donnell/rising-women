from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import ListView, CreateView, FormView
from django.contrib import messages
from .models import Mentor, Category, Subcategory
# from .forms import MentorApplicationForm

# Create your views here.


class MentorsList(ListView):
    """
    RENDER ALL THE MENTORS THAT HAVE BEEN VERIFIED AND APPROVED TO JOIN AS
    """
    model = Mentor
    queryset = Mentor.objects.filter(verified=True).order_by("-joined")
    template_name = "mentors-list.html"


class MentorDetail(CreateView):
    """
    RENDER THE DETAILS PAGE OF THE SELECTED MENTOR
    """
    model = Mentor

    def get(self, request, slug, *args, **kwargs):
        model = Mentor
        queryset = model.objects.filter(verified=True)
        mentor = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "mentor-detail.html",
            {
               "mentor": mentor,
            },
        )


# class MentorApplicationForm(CreateView):
#     form_class = MentorApplicationForm
#     template_name = 'mentor-application.html'
#     success_url = 'thanks'


# def thankPage(request):

#     return render(request, 'thanks.html')


class MentorsFilters(ListView):
    model = Mentor
    template_name = "categories.html"

    def get_queryset(self):
        queryset = Mentor.objects.filter(category=mentor.category)
        return queryset
