"""Build the static nbsystems.dev pages from the Markdown sources in src/.

Run: uv run --with markdown python build.py
Output goes to docs/ (served by GitHub Pages).
"""
import html
import pathlib

import markdown

ROOT = pathlib.Path(__file__).parent
OUT = ROOT / "docs"

PAGES = {
    "privacy": (["src/privacy.md"], "nbOS Launcher Privacy Policy"),
    "licenses": (["src/licenses.md", "src/third-party.md", "src/third-party-mit.md"], "nbOS licenses"),
    "nerdbase-backup": (["src/nerdbase-backup.md"], "nerdbase-backup"),
    "nerdbase-backup-privacy": (["src/nerdbase-backup-privacy.md"], "nerdbase-backup Privacy Policy"),
}

# Repository-relative links in the copied notices point into the (private) source repository; on the site they
# refer to sections of the same page.
LINK_REWRITES = {
    "[`LICENSES/THIRD_PARTY_MIT.md`](LICENSES/THIRD_PARTY_MIT.md)": "the Third-party MIT licenses section below",
    "[`ASSET_LICENSES.md`](ASSET_LICENSES.md)": "the Visual asset licenses section above",
    "[`THIRD_PARTY.md`](../THIRD_PARTY.md)": "the Third-party components section above",
    "[`LICENSE`](../LICENSE)": "the nbOS MIT license",
}

STYLE = """
:root { color-scheme: dark light; --bg:#11121b; --fg:#e4e4ee; --muted:#9698aa; --accent:#be96ff; --line:#2c2e40; }
@media (prefers-color-scheme: light) { :root { --bg:#f6f6fa; --fg:#1b1c26; --muted:#5a5c6e; --accent:#6a3fc8; --line:#d9d9e4; } }
* { box-sizing: border-box; }
body { margin:0; background:var(--bg); color:var(--fg); font:16px/1.6 ui-monospace,"JetBrains Mono","Noto Sans Mono",monospace; }
main { max-width: 46rem; margin: 0 auto; padding: 2.5rem 1.25rem 4rem; }
header { display:flex; justify-content:space-between; align-items:baseline; flex-wrap:wrap; gap:.5rem; border-bottom: 1px solid var(--line); margin-bottom: 2rem; padding-bottom: .75rem; }
header a { color: var(--accent); text-decoration: none; font-weight: 700; }
nav a { color: var(--muted); margin-left: 1rem; font-size: .9rem; }
h1 { font-size: 1.6rem; line-height: 1.25; } h2 { font-size: 1.2rem; margin-top: 2.2rem; } h3 { font-size: 1.05rem; }
a { color: var(--accent); } code { font-size: .92em; color: var(--muted); }
blockquote { margin: 1rem 0; padding-left: 1rem; border-left: 3px solid var(--line); color: var(--muted); }
li { margin: .35rem 0; } footer { margin-top: 3rem; color: var(--muted); font-size: .85rem; }
"""


def page(title: str, body: str, up: str = "", drive: bool = False) -> str:
    navigation = (f'<a href="{up}nerdbase-backup/">About</a><a href="{up}nerdbase-backup-privacy/">Privacy</a>'
                  if drive else f'<a href="{up}privacy/">Privacy</a><a href="{up}licenses/">Licenses</a>')
    contact = ('Maintainer: <a href="https://github.com/nerdislb">nerdislb</a> · '
               '<a href="https://github.com/nerdislb/nbsystems.dev/issues">General questions</a>'
               if drive else 'Contact: <a href="mailto:support@nbsystems.dev">support@nbsystems.dev</a> ·\n'
               'privacy: <a href="mailto:privacy@nbsystems.dev">privacy@nbsystems.dev</a> ·\n'
               'security: <a href="mailto:security@nbsystems.dev">security@nbsystems.dev</a>')
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<style>{STYLE}</style>
</head>
<body>
<main>
<header><a href="{up or './'}">nbsystems.dev</a><nav>{navigation}</nav></header>
{body}
<footer>{contact}</footer>
</main>
</body>
</html>
"""


INDEX = """<h1>nbOS Launcher</h1>
<p>A calm Android launcher inspired by terminal interfaces: an O1 home with clock rings, a ring timer,
favorites and native Android widgets. Currently in closed beta on Google Play.</p>
<ul>
<li><a href="privacy/">Privacy policy</a></li>
<li><a href="licenses/">Licenses (visual assets and third-party notices)</a></li>
</ul>
"""


def main() -> None:
    OUT.mkdir(exist_ok=True)
    (OUT / ".nojekyll").write_text("")
    (OUT / "index.html").write_text(page("nbsystems.dev", INDEX))
    for slug, (sources, title) in PAGES.items():
        text = "\n\n".join((ROOT / src).read_text() for src in sources)
        for old, new in LINK_REWRITES.items():
            text = text.replace(old, new)
        body = markdown.markdown(text, extensions=["sane_lists"])
        (OUT / slug).mkdir(exist_ok=True)
        (OUT / slug / "index.html").write_text(page(title, body, up="../", drive=slug.startswith("nerdbase-backup")))
        print("built", slug)


if __name__ == "__main__":
    main()
