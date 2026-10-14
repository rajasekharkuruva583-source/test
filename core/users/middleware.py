from django.shortcuts import redirect
from django.urls import reverse

class PrivacyConsentMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Bypass for unauthenticated & consent pages
        if not request.user.is_authenticated:
            return self.get_response(request)

        consent_path = reverse("users:privacy")
        exempt_paths = {consent_path, reverse("users:logout"), reverse("users:login")}
        if request.path in exempt_paths or request.path.startswith("/admin"):
            return self.get_response(request)

        try:
            consent = request.user.privacyconsent
            if not consent.consent_given:
                return redirect("users:privacy")
        except Exception:
            return redirect("users:privacy")

        return self.get_response(request)
