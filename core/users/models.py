
# Create your models here.

from django.conf import settings
from django.db import models

class PrivacyConsent(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    consent_given = models.BooleanField(default=False)
    consent_timestamp = models.DateTimeField(auto_now_add=True)
    data_sharing = models.BooleanField(default=False)   # analytics sharing
    data_retention_days = models.PositiveIntegerField(default=30)

    def __str__(self):
        return f"PrivacyConsent(user={self.user.username}, consent={self.consent_given})"
