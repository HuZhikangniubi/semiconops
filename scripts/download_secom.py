from __future__ import annotations
import hashlib, json, shutil, urllib.request, zipfile
from datetime import datetime, timezone
from pathlib import Path

URL = "https://archive.ics.uci.edu/static/public/179/secom.zip"
DOI = "10.24432/C54305"
LICENSE = "CC BY 4.0"
ROOT = Path(__file__).resolve().parents[1]
DOWNLOAD_DIR = ROOT / "data" / "external"
RAW_DIR = ROOT / "data" / "raw" / "secom"
MANIFEST_DIR = ROOT / "data" / "manifests"
ZIP_PATH = DOWNLOAD_DIR / "secom.zip"
MANIFEST_PATH = MANIFEST_DIR / "secom.json"

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as file:
        for chunk in iter(lambda: file.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main() -> None:
    DOWNLOAD_DIR.mkdir(parents=True, exist_ok=True)
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    MANIFEST_DIR.mkdir(parents=True, exist_ok=True)
    if not ZIP_PATH.exists():
        temp = ZIP_PATH.with_suffix(".part")
        try:
            with urllib.request.urlopen(URL, timeout=60) as response, temp.open("wb") as output:
                shutil.copyfileobj(response, output)
            temp.replace(ZIP_PATH)
        except Exception:
            temp.unlink(missing_ok=True)
            raise
    archive_hash = sha256_file(ZIP_PATH)
    if MANIFEST_PATH.exists():
        previous = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        expected = previous.get("sha256")
        if expected and expected != archive_hash:
            raise RuntimeError("Archive hash differs from the existing manifest.")
    with zipfile.ZipFile(ZIP_PATH) as archive:
        archive.extractall(RAW_DIR)
    manifest = {
        "dataset": "SECOM",
        "uci_id": 179,
        "source_url": URL,
        "doi": DOI,
        "license": LICENSE,
        "downloaded_at_utc": datetime.now(timezone.utc).isoformat(),
        "archive_size_bytes": ZIP_PATH.stat().st_size,
        "sha256": archive_hash,
        "limitations": [
            "Features are anonymous and must not be assigned process semantics.",
            "Prediction and SHAP are not root-cause or causal proof.",
            "Raw data is excluded from Git.",
        ],
    }
    MANIFEST_PATH.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
