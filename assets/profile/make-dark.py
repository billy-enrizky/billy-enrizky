# /// script
# requires-python = ">=3.11"
# ///
"""Generate the dark banner project from the light one.

The two projects differ only in six colour variables, so the dark project is
written from the light source, never edited by hand. Run: uv run make-dark.py
"""
import json
import logging
import pathlib
import re
import shutil

logging.basicConfig(level=logging.INFO, format="%(message)s")
log = logging.getLogger("make-dark")

LIGHT = {
    "--paper": "#f1f1f1",
    "--plate": "#fafafa",
    "--ink": "#101010",
    "--muted": "#595959",
    "--accent": "#b83a1f",
    "--rule": "#d6d6d6",
}
DARK = {
    "--paper": "#101010",
    "--plate": "#191919",
    "--ink": "#f1f1f1",
    "--muted": "#b4b4b4",
    "--accent": "#f08a67",
    "--rule": "#373737",
}

HERE = pathlib.Path(__file__).resolve().parent
LIGHT_DIR = HERE
DARK_DIR = HERE.parent / "profile-dark"

source = (LIGHT_DIR / "index.html").read_text(encoding="utf-8")
for name, value in LIGHT.items():
    if not re.search(rf"{re.escape(name)}:\s*{re.escape(value)};", source):
        raise SystemExit(f"{name} is not the light value; refusing to run on a dark source")

output = source
for name, value in DARK.items():
    output, count = re.subn(
        rf"({re.escape(name)}:\s*)#[0-9a-fA-F]{{6}};",
        lambda m, value=value: f"{m.group(1)}{value};",
        output,
        count=1,
    )
    assert count == 1, name

DARK_DIR.mkdir(parents=True, exist_ok=True)
(DARK_DIR / "index.html").write_text(output, encoding="utf-8")

shutil.copytree(LIGHT_DIR / "assets", DARK_DIR / "assets", dirs_exist_ok=True)
shutil.copy(LIGHT_DIR / "hyperframes.json", DARK_DIR / "hyperframes.json")
shutil.copy(LIGHT_DIR / ".gitignore", DARK_DIR / ".gitignore")

package = json.loads((LIGHT_DIR / "package.json").read_text(encoding="utf-8"))
package["name"] = "github-profile-visuals-dark"
package["scripts"]["render"] = package["scripts"]["render"].replace(
    "--output profile-focus.gif", "--output profile-focus-dark.gif"
)
(DARK_DIR / "package.json").write_text(json.dumps(package, indent=2) + "\n", encoding="utf-8")

meta = {"id": "github-profile-visuals-dark", "name": "GitHub Profile Visuals (dark)"}
(DARK_DIR / "meta.json").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")

log.info("dark project written to %s", DARK_DIR.name)
