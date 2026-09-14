#!/usr/bin/env python3
"""Create a public-safe zip by excluding third-party raw/source image buckets."""
import sys, zipfile
from pathlib import Path

if len(sys.argv)!=3:
    raise SystemExit("usage: build_public_release.py source_dir output.zip")
src=Path(sys.argv[1]).resolve(); out=Path(sys.argv[2]).resolve()
exclude_parts={"source_images","raw_images","user_local_assets"}
image_ext={".png",".jpg",".jpeg",".webp",".gif",".bmp",".tif",".tiff"}
with zipfile.ZipFile(out,"w",zipfile.ZIP_DEFLATED) as z:
    for p in src.rglob("*"):
        if not p.is_file(): continue
        rel=p.relative_to(src)
        parts=set(rel.parts)
        if (parts & exclude_parts) and p.suffix.lower() in image_ext:
            continue
        z.write(p, rel)
print(out)
