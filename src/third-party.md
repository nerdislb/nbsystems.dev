# Third-party components

## Cutaway clock arithmetic

The Cutaway clock lineage includes time-derived ring geometry and clock arithmetic
adapted from Dumidu's MIT-licensed
[Orbital Lock](https://github.com/dumidulkdev/omarchy-orbital-lock), reviewed at
commit `6639304d250da02dc3e9771dec7a9c0fc0b87cb2`.

O1 is now the only Home clock. The legacy Frame Cutaway implementation was
removed during slimming; its attribution and MIT notice remain with the
Cutaway lineage.
The former full-screen `ORBIT CENTER`, `ORBIT GREETER`, and `RADIAL HALF`
prototypes, their glass renderer, placement system, and radial presentation were
moved to the separate `nbclocklauncher` prototype. Orbital Lock's session-lock,
PAM, wake, idle, and authentication controllers are not used. nbOS remains an
ordinary Android launcher and does not replace Android Keyguard.

The applicable MIT notice is reproduced in
[`LICENSES/THIRD_PARTY_MIT.md`](LICENSES/THIRD_PARTY_MIT.md).

## Catppuccin palette values

The project-original Topographic Fold wallpapers use color values from
Catppuccin 1.8.0. The pinned palette source, provenance, and Catppuccin MIT
license are retained under `wallpapers/sources/catppuccin/`. No upstream
wallpaper or other visual asset is included. The generated wallpaper license
and attribution are documented separately in [`ASSET_LICENSES.md`](ASSET_LICENSES.md).
