from django.http import HttpResponse


def index(request):
    return HttpResponse("Test: Music Album Guide Backend is now running;")