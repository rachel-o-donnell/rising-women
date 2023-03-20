from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm
from .models import Contact


def contact_view(request):
    """
    View function for the contact form.
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            messages.success(request, 'Thank you for contacting us!')
            return redirect('contact_success')

    else:
        form = ContactForm()

    return render(request, 'contact_form.html', {'form': form})


def contact_success_view(request):
    """
    View function for the contact success page.
    """
    return render(request, 'contact_success.html')
