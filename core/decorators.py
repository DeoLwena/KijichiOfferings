from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from functools import wraps

def role_required(allowed_roles = []):
    def decorator(view_func):
        @wraps(view_func)
        @login_required()
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name__in=allowed_roles).exists():
                return view_func(request, *args, **kwargs)
            else:
                return redirect('login')
        return wrapper
    return decorator