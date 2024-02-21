from django.urls import path
from django.urls import register_converter

from django_passbook.views import register_pass, latest_version, registrations, log


class PassTypeConverter:
    regex = r'[a-zA-Z0-9.]+'

    def to_python(self, value):
        return value

    def to_url(self, value):
        return value

register_converter(PassTypeConverter, "passtype")

urlpatterns = [
    path('v1/devices/<slug:device_library_id>/registrations/<passtype:pass_type_id>/<slug:serial_number>/', register_pass),
    path('v1/devices/<slug:device_library_id>/registrations/<passtype:pass_type_id>/<slug:serial_number>', register_pass),
    path('v1/devices/<slug:device_library_id>/registrations/<passtype:pass_type_id>/', registrations),
    path('v1/passes/<passtype:pass_type_id>/<slug:serial_number>/', latest_version),
    path('v1/log', log),
]
