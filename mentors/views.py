from django.shortcuts import render, redirect, reverse, get_object_or_404
# from django.views import generic, View
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Mentor, Category, Subcategory


class MentorsList(ListView):
    """ RENDER ALL THE AVAILABLE VERIFIED MENTORS AVAILABLE """
    model = Mentor
    queryset = Mentor.objects.filter(verified=True).order_by("-joined")
    template_name = "mentors-list.html"


class MentorDetail(DetailView):
    """ RENDER THE DETAILS PAGE OF THE SELECTED MENTOR """

    model = Mentor
    template_name = 'mentor-detail.html'
    slug_url_kwarg = 'mentor_slug'

    def get_object(self, queryset=None):
        queryset = Mentor.objects.filter(slug=self.kwargs['mentor_slug'],
                                         verified=True)
        obj = get_object_or_404(queryset)
        return obj


def mentor_search(request):
    query = request.GET.get('q')
    category = request.GET.get('category')
    subcategory = request.GET.get('subcategory')
    if query:
        # Search mentors by name or expertise
        mentors = Mentor.objects.filter(Q(name__icontains=query) |
                                        Q(expertise__icontains=query))
    elif category:
        # Filter mentors by category
        mentors = Mentor.objects.filter(category__name=category)
        if subcategory:
            # Filter mentors by subcategory
            mentors = mentors.filter(subcategory__name=subcategory)
    else:
        # If no query or filter, display all mentors
        mentors = Mentor.objects.all()
    # Get all categories and subcategories for displaying in the search form
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()
    context = {'mentors': mentors, 'categories': categories,
               'subcategories': subcategories}
    return render(request, 'mentor_search.html', context)
