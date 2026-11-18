#!/usr/bin/env python3
"""
Entrypoint for make.fun competition news-image-20261117.

Reads MAKEFUN_OUTPUT_DIR (defaulting to '/output'), ensures the directory
exists, and copies the accompanying entry.png image to <output>/entry.png.
"""

import os
import shutil


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    src_path = os.path.join(base_dir, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

    if not os.path.isfile(src_path):
        raise SystemExit(f"Error: required image file not found: {src_path}")

    os.makedirs(output_dir, exist_ok=True)
    dst_path = os.path.join(output_dir, "entry.png")

    shutil.copy2(src_path, dst_path)
    print(f"Successfully copied image to {dst_path}")


if __name__ == "__main__":
    main()
