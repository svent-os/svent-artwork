# SventOS branding

**Logo:** a dark blue / slate field with a **red orca**.

**Palette** (`palette.json`):

| token | hex | use |
|---|---|---|
| `field_dark` | `#0d1b2a` | dark background field |
| `field_slate` | `#2a3444` | gray/slate field |
| `orca_body` | `#1b2b44` | orca body (dark blue) |
| `orca_red` | `#e23b3b` | orca accent / red |
| `accent` | `#e23b3b` | UI accent (red) |
| `text` | `#e6edf3` | light text |

Adjust the hex values to your exact art; everything else reads from here.

## Files you must provide (currently empty placeholders)

Export these from `logo/logo.svg` into `assets/logo/`. All PNG, transparent
background unless noted. These are the names the system installs to
`/usr/share/svent/logo/`.

| file | size | purpose |
|---|---|---|
| `logo.png` | 1024×1024 | primary logo, transparent |
| `logo-white.png` | 1024×1024 | monochrome white (for dark UIs) |
| `logo-black.png` | 1024×1024 | monochrome black (for light UIs) |
| `logo-on-dark.png` | 1024×1024 | full-color logo on the dark field |
| `logo-on-light.png` | 1024×1024 | full-color logo on light background |
| `icon-16.png` … `icon-256.png` | 16/32/48/64/128/256 | app/menu/window icons |

The **wallpapers are already real** (your 3 orca images, dark, landscape + portrait):

```
assets/backgrounds/svent/landscape/svent-orca-dark.png         (default, one orca)
assets/backgrounds/svent/landscape/svent-two-orcas-dark.png    (two orcas)
assets/backgrounds/svent/landscape/svent-orca-waves-dark.png   (orca in waves)
assets/backgrounds/svent/portrait/svent-orca-dark.png
assets/backgrounds/svent/portrait/svent-two-orcas-dark.png
assets/backgrounds/svent/portrait/svent-orca-waves-dark.png
```

`orca-dark` is the default. svent-core's `svent-wallpaper` selector currently
uses `DEFAULT_CHOICE=ridge-dark`, so update that line to `orca-dark` in
`svent-core/bin/svent-wallpaper`.

Light variants (`svent-*-light.png`) are optional; add them later if you want a
light theme — the selector will list them automatically.
