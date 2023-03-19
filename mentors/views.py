from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib import messages
from .models import Mentor, Category, Subcategory
from django.db.models import Q
from django.db.models.functions import Lower


class MentorsList(ListView):
    """ RENDER ALL THE AVAILABLE VERIFIED MENTORS INCLUDING SEARCH QUERIES """

    model = Mentor
    queryset = Mentor.objects.filter(verified=True).order_by("-joined")
    template_name = "mentors-list.html"

    def mentor_search(self, request):
        mentors = self.queryset
        query = None
        categories = None
        subcategories = None

        if request.GET:
            # Handle sorting
            sort_key = request.GET.get('sort')
            if sort_key == 'name':
                sort_key = 'lower_name'
                mentors = mentors.annotate(lower_name=Lower('name'))

            direction = request.GET.get('direction')
            if direction == 'desc':
                sort_key = f'-{sort_key}'
            if sort_key:
                mentors = mentors.order_by(sort_key)

            # Handle filtering
            category_names = request.GET.getlist('category')
            if category_names:
                mentors = mentors.filter(category__name__in=category_names)
                categories = Category.objects.filter(name__in=category_names)

            subcategory_names = request.GET.getlist('subcategory')
            if subcategory_names:
                mentors = mentors.filter(
                    subcategory__name__in=subcategory_names)
                subcategories = Subcategory.objects.filter(
                    name__in=subcategory_names)

            # Handle search
            if 'q' in request.GET:
                query = request.GET['q']
                if not query:
                    messages.error(request,
                                   "You didn't enter any search criteria!")
                queries = (Q(name__icontains=query) |
                           Q(expertise__icontains=query) |
                           Q(bio__icontains=query))
                mentors = mentors.filter(queries)

        mentors_count = mentors.count()  # Count the number of mentors

        context = {
            'mentors': mentors,
            'categories': categories,
            'subcategories': subcategories,
            'query': query,
            'mentors_count': mentors_count,  # Pass the count to the context
        }

        return render(request, self.template_name, context)


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
