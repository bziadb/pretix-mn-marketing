from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

from pretix import __version__ as version


class MnMarketingApp(AppConfig):
    name = 'pretix_mn_marketing'
    label = 'mn_marketing'
    verbose_name = _("MN Marketing landing page")

    class PretixPluginMeta:
        name = _("MN Marketing")
        author = "MN Marketing"
        version = version
        category = "FEATURE"
        featured = False
        description = _(
            "Replaces the default pretix landing page with the MN Marketing branding."
        )

    def ready(self):
        # Auto-register the branding middleware so the control-panel top-bar
        # icon is swapped without any admin action.
        from django.conf import settings
        mw = 'pretix_mn_marketing.middleware.MnBrandingMiddleware'
        middleware = list(settings.MIDDLEWARE)
        if mw not in middleware:
            middleware.append(mw)
            settings.MIDDLEWARE = middleware
