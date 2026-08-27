"""
Rewrites the pretix top-bar icon in every /control/ HTML response to the MN
Marketing "mn" arch logo, embedded as an inline data-URI so no server-side
static file needs to be swapped and no collectstatic step is required.
"""
import base64
import re

# Blue "m" arch + magenta "n" arch, MN brand colors, transparent background.
_MN_SVG = (
    b'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 60">'
    b'<path fill="#447FB9" d="M 6 55 L 6 22 C 6 12, 16 6, 25 6 C 34 6, 44 12, 44 22 '
    b'L 44 55 L 33 55 L 33 24 C 33 20, 29 17, 25 17 C 21 17, 17 20, 17 24 L 17 55 Z"/>'
    b'<path fill="#731183" d="M 48 55 L 48 22 C 48 12, 58 6, 67 6 C 76 6, 86 12, 86 22 '
    b'L 86 55 L 75 55 L 75 24 C 75 20, 71 17, 67 17 C 63 17, 59 20, 59 24 L 59 55 Z"/>'
    b'</svg>'
)
_DATA_URI = 'data:image/svg+xml;base64,' + base64.b64encode(_MN_SVG).decode('ascii')

# Matches the icon URL with or without a Manifest hash suffix.
_ICON_RE = re.compile(
    rb'/static/pretixbase/img/pretix-icon-white-mini(?:\.[a-f0-9]+)?\.svg'
)


class MnBrandingMiddleware:
    """Swap pretix icon → MN logo in the control-panel top bar."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Only touch control-panel HTML pages.
        if not request.path.startswith('/control'):
            return response
        ctype = response.get('Content-Type', '')
        if 'text/html' not in ctype:
            return response
        if not hasattr(response, 'content'):
            return response

        new_content = _ICON_RE.sub(_DATA_URI.encode('ascii'), response.content)
        if new_content != response.content:
            response.content = new_content
            if response.get('Content-Length'):
                response['Content-Length'] = str(len(response.content))

        return response
