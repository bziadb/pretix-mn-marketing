from django.utils.translation import get_language
from django.views.generic import TemplateView

from .translations import RTL_LANGS, get_contact_url, get_translation


class LandingPageView(TemplateView):
    template_name = 'pretixplugins/mn_marketing/index.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        lang = get_language() or 'en'
        ctx['lang_code'] = lang
        ctx['is_rtl'] = lang.split('-')[0] in RTL_LANGS
        ctx['t'] = get_translation(lang)
        ctx['contact_url'] = get_contact_url(lang)
        return ctx
