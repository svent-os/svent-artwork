# svent-artwork

SventOS branding package: wallpapers + logo. Static assets only — no generators.
Installs to the paths the rest of SventOS expects:

- wallpapers → `/usr/share/backgrounds/svent/{landscape,portrait}/svent-*.png`
- logo → `/usr/share/svent/logo/*.png` + `palette.json`

The `svent-wallpaper` selector that reads these lives in **svent-core** (not
here). The XFCE and bspwm sessions call it to set the wallpaper.

## Layout

```
assets/
  backgrounds/svent/landscape/*.png   REAL (orca, two-orcas, orca-waves; dark)
  backgrounds/svent/portrait/*.png    REAL (orca, two-orcas, orca-waves; dark)
  logo/*.png                          PLACEHOLDERS (empty) — drop your orca logo
  logo/palette.json                   brand colors
logo/logo.svg                         master logo source (empty placeholder)
palette.json                          brand colors (source of truth)
bin/stamp-metadata                    stamps Author=z1rov on the PNGs (run on VM)
debian/                               packaging (produces svent-artwork_*.deb)
```

See `BRANDING.md` for the exact logo files to provide and the color tokens.

## Status

- ✅ Wallpapers: real (ridge/dunes/peak, dark, landscape + portrait).
- ⬜ Logo: the `assets/logo/*.png` and `logo/logo.svg` are **empty placeholders**.
  Fill them with the real orca logo before building (otherwise the package ships
  empty logo files).

## Build / publish (on the Debian VM)

```bash
# 1) (once) author metadata on the images
sudo apt install -y libimage-exiftool-perl
./bin/stamp-metadata

# 2) build the .deb
export TMPDIR=/var/tmp
dpkg-buildpackage -b -us -uc

# 3) import + publish to the APT repo
reprepro -b ~/pkgs remove rolling svent-artwork 2>/dev/null
reprepro -b ~/pkgs includedeb rolling ../svent-artwork_0.1.0_all.deb
svent-pkg publish

# 4) test
sudo apt update && sudo apt install -y svent-artwork
svent-wallpaper --list        # should list: orca-dark, two-orcas-dark, orca-waves-dark
```

The default wallpaper is `orca-dark`. svent-core's `svent-wallpaper` selector
still has `DEFAULT_CHOICE=ridge-dark`; change that line to `orca-dark`.

Bump `debian/changelog` version whenever you change the assets.
