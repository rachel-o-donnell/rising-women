from django.shortcuts import render


def index(request):
    return render(request, 'home/index.html')


def handler404(request, exception):
    """ Custom 404 page """
    return render(request, "errors/404.html", status=404)


def handler500(request):
    """ Custom 500 page """
    return render(request, "errors/500.html", status=500)


def handler400(request, exception):
    """ Custom 400 page """
    return render(request, "errors/400.html", status=400)
