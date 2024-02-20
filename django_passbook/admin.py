from apns2.client import APNsClient
from apns2.payload import Payload
from django.contrib import admin
from django_passbook.models import Pass, Registration, Log
from django_passbook import settings


def push_update(modeladmin, request, queryset):
    for r in queryset.all():
        topic = settings.PASSBOOK_CERT_TOPIC
        client = APNsClient(settings.PASSBOOK_CERT_KEY, use_sandbox=False, use_alternative_port=False)
        client.send_notification(r.push_token, Payload(), topic)

push_update.short_description = "Send a push notification to update Pass"


class RegistrationAdmin(admin.ModelAdmin):
    actions = [push_update]

class LogAdmin(admin.ModelAdmin):
    list_display = ('id', 'message')

admin.site.register(Pass)
admin.site.register(Registration, RegistrationAdmin)
admin.site.register(Log, LogAdmin)
