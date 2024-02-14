from django.urls import path

from django_passbook.views import register_pass, latest_version, registrations, log

urlpatterns = [
    path('v1/devices/<slug:device_library_id>/registrations/<slug:pass_type_id>/<slug:serial_number>', register_pass),
    path('v1/devices/<slug:device_library_id>/registrations/<slug:pass_type_id>/<slug:serial_number>', register_pass),
    path('v1/devices/<slug:device_library_id>/registrations/<slug:pass_type_id>', registrations),
    path('v1/passes/<slug:pass_type_id>/<slug:serial_number>', latest_version),
    path('v1/log', log),
]
