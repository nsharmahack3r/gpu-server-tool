# server-res

Downloads all files from a Google Drive folder into a local directory.

## Setup

Install dependencies (requires [uv](https://docs.astral.sh/uv/)):

```bash
uv sync
```

Configure the environment:

```bash
cp .sample.env .env
```

Then edit `.env`:

- `GOOGLE_DRIVE_SOURCE_DIR` — Drive folder ID (e.g. `1aBcD3fGhIjKlMnOpQrStUvWxYz1234567890`) or full folder URL (`https://drive.google.com/drive/folders/<id>`). The folder must be shared with "Anyone with the link".
- `LOCAL_DEST_PATH` — local directory to download into (created if missing).

## Usage

```bash
uv run download.py
```

Files are downloaded into `LOCAL_DEST_PATH`, preserving the folder's structure.

## Troubleshooting

- **Download fails** — make sure the folder is shared as "Anyone with the link" (Drive: Share → General access). The script does not authenticate with Google.
- **Config errors** — both variables must be set in `.env`.
