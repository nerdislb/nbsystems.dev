# nbsystems.dev

Static pages for nbsystems.dev: the nbOS Launcher privacy policy and visual asset licenses.

- Sources: `src/privacy.md` (copy of `PRIVACY.md` from the nbOS repository) and `src/licenses.md`, `src/third-party.md`, `src/third-party-mit.md`
  (`ASSET_LICENSES.md`, `THIRD_PARTY.md`, `LICENSES/THIRD_PARTY_MIT.md`).
- Build: `uv run --with markdown python build.py` writes `docs/`, which GitHub Pages serves.
- Update the policy in the nbOS repository first, copy it to `src/`, rebuild and commit both.
