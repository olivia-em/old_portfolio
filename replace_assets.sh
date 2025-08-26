#!/usr/bin/env bash

echo "=== Complete Glitch Asset Replacement Script ==="

MAP_FILE="asset_map.txt"

if [[ ! -f "$MAP_FILE" ]]; then
  echo "Error: mapping file $MAP_FILE not found."
  exit 1
fi

count=0

while IFS= read -r line; do
  # skip empty or comment lines
  [[ -z "$line" || "$line" =~ ^# ]] && continue

  filename=$(echo "$line" | awk '{print $1}')
  local_path=$(echo "$line" | awk '{print $2}')

  echo "Processing: $filename"
  count=$((count+1))

  # Replace in HTML/template contexts (src, href with double quotes)
  find src -type f \( -name "*.md" -o -name "*.njk" -o -name "*.html" \) \
    -exec sed -i.bak "s#https://cdn\.glitch\.[^\"]*${filename//\%/\\%}[^\"]*#{{ \"$local_path\" | url }}#g" {} +

  # Replace in HTML/template contexts (src, href with single quotes)
  find src -type f \( -name "*.md" -o -name "*.njk" -o -name "*.html" \) \
    -exec sed -i.bak "s#https://cdn\.glitch\.[^']*${filename//\%/\\%}[^']*#{{ \"$local_path\" | url }}#g" {} +

  # Markdown image syntax
  find src -type f -name "*.md" \
    -exec sed -i.bak "s#](https://cdn\.glitch\.[^)]*${filename//\%/\\%}[^)]*)#]({{ \"$local_path\" | url }})#g" {} +

  # Markdown link syntax
  find src -type f -name "*.md" \
    -exec sed -i.bak "s#\[\([^]]*\)\](https://cdn\.glitch\.[^)]*${filename//\%/\\%}[^)]*)#[\1]({{ \"$local_path\" | url }})#g" {} +

done < "$MAP_FILE"

echo ""
echo "=== Replacement Complete! ==="
echo ""
echo "Summary:"
echo "- Processed $count different assets"
echo "- Created .bak backup files for all modified files"
echo ""
echo "Next steps:"
echo "1. Test your build: NODE_ENV=production npm run build"
echo "2. Check results: grep -r 'assets.*png\\|assets.*jpg\\|assets.*mp4' src/"
echo "3. Remove .bak files when satisfied: find src -name '*.bak' -delete"
echo ""
echo "Files that were modified:"
find src -name "*.bak" | wc -l | xargs echo "Total backup files created:"

