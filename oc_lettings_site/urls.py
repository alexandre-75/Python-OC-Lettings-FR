from django.contrib import admin
from django.urls import path, include
from . import views


def trigger_error(request):
    """For sentry test"""
    try:
        division_by_zero = 1 / 0
    except ZeroDivisionError:
        division_by_zero = print("Cannot divide by zero.")
    return division_by_zero


urlpatterns = [
    path('', views.index, name='index'),
    path("lettings/", include("lettings.urls")),
    path("profiles/", include("profiles.urls")),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error)
]
