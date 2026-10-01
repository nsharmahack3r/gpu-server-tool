import os
import re
import sys
from pathlib import Path

import gdown
from dotenv import load_dotenv

FOLDER_URL = "https://drive.google.com/drive/folders/{}"


def extract_folder_id(source: str) -> str:
    source = source.strip()
    match = re.search(r"/folders/([A-Za-z0-9_-]+)", source)
    if match:
        return match.group(1)
    if re.fullmatch(r"[A-Za-z0-9_-]+", source):
        return source
    raise ValueError(
        f"GOOGLE_DRIVE_SOURCE_DIR must be a Drive folder ID or a folder URL, got: {source!r}"
    )


def main() -> int:
    load_dotenv()

    source = os.getenv("GOOGLE_DRIVE_SOURCE_DIR")
    dest = os.getenv("LOCAL_DEST_PATH")

    if not source:
        print("Error: GOOGLE_DRIVE_SOURCE_DIR is not set in .env", file=sys.stderr)
        return 1
    if not dest:
        print("Error: LOCAL_DEST_PATH is not set in .env", file=sys.stderr)
        return 1

    folder_url = FOLDER_URL.format(extract_folder_id(source))
    dest_path = Path(dest).expanduser().resolve()
    dest_path.mkdir(parents=True, exist_ok=True)

    print(f"Downloading folder: {folder_url}")
    print(f"Destination: {dest_path}")

    files = gdown.download_folder(
        url=folder_url,
        output=str(dest_path),
        quiet=False,
    )

    if not files:
        print(
            "Error: download failed. Check that the folder ID is correct and the "
            "folder is shared publicly (Anyone with the link).",
            file=sys.stderr,
        )
        return 1

    print(f"Done. Downloaded {len(files)} file(s) to {dest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
