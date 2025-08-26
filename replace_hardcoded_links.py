#!/usr/bin/env python3
import re
import pathlib
import shutil

# Pattern to match Liquid variable usage that should get the | url filter
# This targets variables that are likely to be local asset paths
asset_var_pattern = re.compile(r'{{\s*([\w.]+\.(?:image|thumbnail|photo|src|asset))\s*}}')

# Pattern for HTML attributes (href/src) with absolute paths
html_pattern = re.compile(r'(href|src)=(["\'])(/[^"\']*)\2')

# Pattern to fix escaped quotes in Liquid tags
escaped_quotes_pattern = re.compile(r"{{(\s*)\\'([^']*)\\'(\s*\|\s*url\s*)}}")

root = pathlib.Path("src")  # adjust as needed

for ext in ("*.html", "*.md", "*.njk"):
    for file in root.rglob(ext):
        text = file.read_text(encoding="utf-8")
        original_text = text
        
        # Process Liquid variables that should use | url filter
        def asset_var_replacer(match):
            var_name = match.group(1)
            # Skip if it already has a filter
            if "| url" in match.group(0):
                return match.group(0)
            # Add the url filter
            return f'{{{{ {var_name} | url }}}}'
        
        text = asset_var_pattern.sub(asset_var_replacer, text)
        
        # Process HTML attributes with absolute paths
        def html_replacer(match):
            attr, quote, path = match.groups()
            # Skip if it's already a liquid tag
            if "{{" in path and "}}" in path:
                return match.group(0)
            # Skip if it's already processed
            if "| url" in path:
                return match.group(0)
            # Transform the path - use regular quotes, not escaped
            return f'{attr}={quote}{{{{ \'{path}\' | url }}}}{quote}'
        
        text = html_pattern.sub(html_replacer, text)
        
        # Fix escaped quotes in existing Liquid tags
        def fix_escaped_quotes(match):
            space1, path, space2_and_filter = match.groups()
            return f'{{{{{space1}\'{path}\'{space2_and_filter}}}}}'
        
        text = escaped_quotes_pattern.sub(fix_escaped_quotes, text)
        
        if text != original_text:
            print(f"✔ Rewrote links in: {file}")
            shutil.copy(file, file.with_suffix(file.suffix + ".bak"))
            file.write_text(text, encoding="utf-8")