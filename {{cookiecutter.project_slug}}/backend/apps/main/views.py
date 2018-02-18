# pylint: disable=unused-argument
from django.shortcuts import render


def bad_request(request, exception=None):
    return render(request, 'errors/bad_request.html', status=400)


def permission_denied(request, exception=None):
    return render(request, 'errors/permission_denied.html', status=403)


def page_not_found(request, exception=None):
    return render(request, 'errors/page_not_found.html', status=404)


def server_error(request):
    return render(request, 'errors/server_error.html', status=500)
