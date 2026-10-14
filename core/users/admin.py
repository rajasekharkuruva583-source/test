
# Register your models here.
from django.contrib import admin
from .models import PrivacyConsent

@admin.register(PrivacyConsent)
class PrivacyConsentAdmin(admin.ModelAdmin):
    list_display = ("user", "consent_given", "data_sharing", "data_retention_days")
    list_filter = ("consent_given", "data_sharing")
    search_fields = ("user__username", "user__email")
