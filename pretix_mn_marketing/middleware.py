"""
Rewrites the pretix top-bar icon in every /control/ HTML response to the actual
MN Marketing logo (loaded from the plugin's own static folder at import time and
embedded as a data-URI). Works without collectstatic and without touching any
pretix files.
"""
import base64
import re
from pathlib import Path

_LOGO_PATH = (
    Path(__file__).resolve().parent
    / "static" / "pretixplugins" / "mn_marketing" / "logo.png"
)

# Load the real MN Marketing color logo once at import time.
try:
    _LOGO_B64 = base64.b64encode(_LOGO_PATH.read_bytes()).decode("ascii")
    _DATA_URI = "data:image/png;base64," + _LOGO_B64
except FileNotFoundError:
    _DATA_URI = ""

# Matches the pretix icon URL, with or without a Manifest hash suffix.
_ICON_RE = re.compile(
    rb"/static/pretixbase/img/pretix-icon-white-mini(?:\.[a-f0-9]+)?\.svg"
)


class MnBrandingMiddleware:
    """Swap the pretix "P" icon in the control-panel top bar for the MN logo."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if not _DATA_URI:
            return response
        if not request.path.startswith("/control"):
            return response
        if "text/html" not in response.get("Content-Type", ""):
            return response
        if not hasattr(response, "content"):
            return response

        new = _ICON_RE.sub(_DATA_URI.encode("ascii"), response.content)
        if new != response.content:
            response.content = new
            if response.get("Content-Length"):
                response["Content-Length"] = str(len(response.content))
        return response
