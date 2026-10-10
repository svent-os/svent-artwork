#!/usr/bin/env python3
import os
import sys
import tempfile
from pathlib import Path

from PIL import Image, PngImagePlugin


def stamp(path):
    with Image.open(path) as image:
        image.load()
        metadata = PngImagePlugin.PngInfo()
        for key, value in image.text.items():
            if key not in {"Author", "Copyright"}:
                metadata.add_itxt(key, value)
        metadata.add_text("Author", "z1rov")
        metadata.add_text("Copyright", "2026 z1rov")
        options = {key: image.info[key] for key in ("icc_profile", "dpi", "exif", "transparency") if key in image.info}
        descriptor, temporary = tempfile.mkstemp(prefix=path.name + ".", suffix=".tmp", dir=path.parent)
        os.close(descriptor)
        try:
            image.save(temporary, format="PNG", pnginfo=metadata, **options)
            os.replace(temporary, path)
        finally:
            Path(temporary).unlink(missing_ok=True)


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent
    directory = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "assets"
    for source in sorted(directory.rglob("*.png")):
        if source.is_symlink():
            continue
        if source.stat().st_size == 0:
            raise ValueError(f"Empty image asset: {source}")
        stamp(source)
        print(f"Stamped {source}")
