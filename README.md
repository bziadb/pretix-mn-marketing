# pretix-mn-marketing

Custom MN Marketing branded landing page for the pretix root URL. Auto-detects the
visitor's language and shows the copy in 34 languages (including RTL for Arabic
and Hebrew). Contact button links language-specifically to the MN-Marketing
information-request page.

## What it replaces

- The default pretix "Hello!" landing page at `/` — replaced with a branded MN
  Marketing card (logo, tagline, Login button, Contact button).
- The tab title becomes "MN Marketing Network".
- A custom favicon is served.

## Limitations (when installed via pip)

The internal, in-source version of this plugin also swaps the pretix logo on the
`/control/login/` page. When installed as an external pip package, that override
does **not** apply because pretix's built-in templates take precedence over
plugin overrides (INSTALLED_APPS ordering). If you want the login page branded
too, you have two options:

1. **Replace the file in-place** on your pretix installation:
   ```bash
   cp your-logo.png $(python -c "import pretix, os; print(os.path.dirname(pretix.__file__))")/static/pretixbase/img/pretix-logo.svg
   ```
2. **Fork pretix** and prepend `pretix_mn_marketing` to `INSTALLED_APPS` before
   `pretix.control` — this is what the in-source version does.

## Installation

```bash
pip install git+https://github.com/bziadb/pretix-mn-marketing.git
python -m pretix migrate  # (no DB tables, but harmless)
systemctl restart pretix
```

Enable it under **any event → Settings → Plugins → MN Marketing landing page**.

Once enabled on at least one event, the landing page is active for the whole
installation (URL-level plugin, not event-scoped in effect).

## Configuration

Edit `pretix_mn_marketing/translations.py` to change copy or add more
language-specific contact URLs.

## License

AGPL-3.0-or-later.
