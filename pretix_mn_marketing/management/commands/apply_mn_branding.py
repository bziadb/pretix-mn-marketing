"""
Apply MN Marketing branding to the pretix installation.

Copies the plugin's white "mn" icon over pretix's built-in top-bar icon, and
optionally updates the instance name shown next to it. Run once after
`pip install`; safe to re-run.

    python -m pretix apply_mn_branding
    python -m pretix apply_mn_branding --instance-name "MN Marketing"
    python -m pretix apply_mn_branding --revert   # restore original icon
"""
import shutil
from pathlib import Path

import pretix
from django.core.management.base import BaseCommand


PRETIX_ROOT = Path(pretix.__file__).parent
TARGET_ICON = PRETIX_ROOT / "static" / "pretixbase" / "img" / "pretix-icon-white-mini.svg"
BACKUP_ICON = TARGET_ICON.with_suffix(".svg.mn_backup")

PLUGIN_ROOT = Path(__file__).resolve().parents[2]
SOURCE_ICON = PLUGIN_ROOT / "static" / "pretixplugins" / "mn_marketing" / "pretix-icon-white-mini.svg"


class Command(BaseCommand):
    help = "Replace the pretix top-bar icon with the MN Marketing logo."

    def add_arguments(self, parser):
        parser.add_argument(
            "--revert", action="store_true",
            help="Restore the original pretix icon (from backup made on first run).",
        )
        parser.add_argument(
            "--instance-name", type=str, default=None,
            help='Also set the site instance-name shown next to the icon '
                 '(writes to /etc/pretix/pretix.cfg — needs write permission).',
        )
        parser.add_argument(
            "--no-collectstatic", action="store_true",
            help="Skip running collectstatic afterwards (do it yourself).",
        )

    def handle(self, *args, **opts):
        if opts["revert"]:
            self._revert()
        else:
            self._apply()

        if opts.get("instance_name"):
            self._set_instance_name(opts["instance_name"])

        if not opts.get("no_collectstatic"):
            self._collectstatic()

        self.stdout.write(self.style.SUCCESS(
            "Done. Restart pretix (systemctl restart pretix-web pretix-worker)."
        ))

    # --- helpers -----------------------------------------------------------

    def _apply(self):
        if not SOURCE_ICON.exists():
            raise SystemExit(f"Plugin icon missing at {SOURCE_ICON}")
        if not TARGET_ICON.exists():
            raise SystemExit(
                f"Target pretix icon not found at {TARGET_ICON}. "
                "Is pretix installed correctly?"
            )
        if not BACKUP_ICON.exists():
            shutil.copy2(TARGET_ICON, BACKUP_ICON)
            self.stdout.write(f"Backed up original icon → {BACKUP_ICON.name}")
        shutil.copy2(SOURCE_ICON, TARGET_ICON)
        self.stdout.write(self.style.SUCCESS(f"Replaced icon at {TARGET_ICON}"))

    def _revert(self):
        if not BACKUP_ICON.exists():
            raise SystemExit(
                "No backup found. Reinstall pretix to restore the original icon."
            )
        shutil.copy2(BACKUP_ICON, TARGET_ICON)
        BACKUP_ICON.unlink()
        self.stdout.write(self.style.SUCCESS("Restored original pretix icon."))

    def _set_instance_name(self, name: str):
        cfg = Path("/etc/pretix/pretix.cfg")
        if not cfg.exists():
            self.stdout.write(self.style.WARNING(
                f"{cfg} not found — please set `instance_name = {name}` "
                "under [pretix] manually."
            ))
            return
        text = cfg.read_text(encoding="utf-8")
        if "instance_name" in text:
            import re
            text = re.sub(
                r"^\s*instance_name\s*=.*$",
                f"instance_name = {name}",
                text,
                flags=re.MULTILINE,
            )
        elif "[pretix]" in text:
            text = text.replace(
                "[pretix]",
                f"[pretix]\ninstance_name = {name}",
                1,
            )
        else:
            text += f"\n[pretix]\ninstance_name = {name}\n"
        try:
            cfg.write_text(text, encoding="utf-8")
            self.stdout.write(self.style.SUCCESS(
                f"Set instance_name = {name} in {cfg}"
            ))
        except PermissionError:
            self.stdout.write(self.style.WARNING(
                f"No write permission on {cfg}. Add manually under [pretix]: "
                f"instance_name = {name}"
            ))

    def _collectstatic(self):
        from django.core.management import call_command
        self.stdout.write("Running collectstatic…")
        call_command("collectstatic", interactive=False, verbosity=0)
        self.stdout.write("collectstatic done.")
