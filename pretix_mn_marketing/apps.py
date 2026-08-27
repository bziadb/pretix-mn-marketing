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
