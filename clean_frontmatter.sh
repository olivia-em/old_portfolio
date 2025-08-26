#!/usr/bin/env bash
# Cleanup front matter asset paths in Markdown files
# Strips {{ ... | url }} and leaves just the /assets/... path

echo "=== Cleaning front matter asset paths in Markdown files... ==="

find src -type f -name "*.md" | while read -r file; do
  echo "Processing: $file"

  # Replace lines like:
  #   thumbnail: {{ "/assets/foo.png" | url }}
  # with:
  #   thumbnail: /assets/foo.png
  sed -i.bak -E 's#(thumbnail:)\s*\{\{\s*"?(/assets/[^"|]+)"?\s*\|\s*url\s*\}\}#\1 \2#' "$file"

  # Same for any "image:" keys
  sed -i.bak -E 's#(image:)\s*\{\{\s*"?(/assets/[^"|]+)"?\s*\|\s*url\s*\}\}#\1 \2#' "$file"
done

echo "=== Cleanup complete! ==="
echo "Backup files created with .bak extension (safe to delete if all looks good)."
