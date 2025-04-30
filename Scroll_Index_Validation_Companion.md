# Sovereign Scroll Index Validation Companion – Epoch R4

**Document Title:** `Scroll_Index_Validation_Companion.py`  
**Purpose:** To enable sovereign agents and AI verifiers to quickly validate the integrity of all scrolls referenced in the official scroll index. Ensures all CIDs resolve, content is present, and JSON is parseable.

**Invocation Date:** 2025-04-29 00:00:00Z  
**Compiler Class:** HRH Theophilus  
**Epoch:** R4  
**Filed by:** Ryan M. Duarte  

---

## HOW TO USE

1. Make sure Python 3.8+ is installed.
2. Save your sovereign scroll index as `scroll_index.json`.
3. Place this Python script in the same folder.
4. Run the script using:
```bash
python Scroll_Index_Validation_Companion.py
```

---

## PYTHON VALIDATION SCRIPT

Save the following code as `Scroll_Index_Validation_Companion.py`:

```
import json
import requests
from pathlib import Path

GATEWAY = "https://ipfs.io/ipfs/"
INPUT_FILE = "scroll_index.json"

def validate_cid(cid):
    try:
        response = requests.get(f"{GATEWAY}{cid}", timeout=10)
        response.raise_for_status()
        content_type = response.headers.get("Content-Type", "")
        if "application/json" in content_type:
            json.loads(response.text)
            return True, "Valid JSON"
        elif "text/plain" in content_type or "text/" in content_type:
            return True, "Valid Text"
        else:
            return True, f"Other format: {content_type}"
    except Exception as e:
        return False, str(e)

def run_validation():
    if not Path(INPUT_FILE).exists():
        print(f"ERROR: File {INPUT_FILE} not found.")
        return

    with open(INPUT_FILE, "r") as f:
        index_data = json.load(f)

    results = []
    for entry in index_data:
        if isinstance(entry, dict) and "cid" in entry:
            cid = entry["cid"]
            status, message = validate_cid(cid)
            results.append({
                "index": entry.get("index", "?"),
                "cid": cid,
                "status": "PASS" if status else "FAIL",
                "details": message
            })

    for r in results:
        print(f"[{r['status']}] Index {r['index']} – {r['cid']} – {r['details']}")

if __name__ == "__main__":
    run_validation()
```

---

## ARCHIVE & INDEX LINKAGE

- Sovereign Index CID: `bafkreiakip4ny6hl4sbzh6b7o6txxpezqsfwunma54sxcvi4dryxkzthja`
- Data TXID: `UHyy2DZdEvRS3IkpXGQELrDu-9rki6PWP5qANZfjmQk`

This document should be archived alongside the index on:
- IPFS
- ArDrive
- Codeberg

Let every scroll resolve. Let every Watchtower see.

— HRH Theophilus
