from django.urls import re_path

from .views import LandingPageView

# Registered under the "plugins" namespace, which is included BEFORE the
# default presale index in maindomain_urlconf. Matching ^$ here therefore
# replaces the built-in landing page.
urlpatterns = [
    re_path(r'^$', LandingPageView.as_view(), name='landing'),
]
