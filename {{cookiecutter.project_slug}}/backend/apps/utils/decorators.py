from django.http import HttpResponseBadRequest


def superuser_login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)
    return wrapper


def admin_login_required(func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_admin:
            return HttpResponseBadRequest()
        return func(request, *args, **kwargs)
    return wrapper
