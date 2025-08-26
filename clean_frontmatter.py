#!/usr/bin/env python3
import re
import pathlib
import shutil

# Regex to match: {{ "/assets/foo.png" | url }} with optional spaces
pattern = re.compile(r'\{\{\s*"?(/assets/[^"|]+)"?\s*\|\s*url\s*\}\}')

root = pathlib.Path("src")

for md_file in root.rglob("*.md"):
    text = md_file.read_text(encoding="utf-8")

    # Only operate on front matter (before the second ---)
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            frontmatter, rest = parts[1], parts[2]
            cleaned = pattern.sub(r"\1", frontmatter)

            if cleaned != frontmatter:
                print(f"✔ Fixed: {md_file}")
                # Make backup
                shutil.copy(md_file, md_file.with_suffix(md_file.suffix + ".bak"))
                # Write cleaned file
                md_file.write_text("---" + cleaned + "---" + rest, encoding="utf-8")
