declare -A assets=(
    ["docblog.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-docblog.png"
    ["cover.png"]="/assets/95731519-6287-4bbd-a281-712ac2b13fef-cover.png"
    ["areyoufree.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-areyoufree.png"
    ["assemblage.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-assemblage.png"
    ["bowl.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-bowl.png"
    ["closet.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-closet.png"
    ["decode1-min.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-decode1-min.png"
    ["decode2-min.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-decode2-min.png"
    ["decode4-min.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-decode4-min.png"
    ["decode5-min.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-decode5-min.png"
    ["justbones.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-justbones.png"
    ["rors.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-rors.png"
    ["sounddevils.png"]="/assets/2decb767-8051-4237-974a-927409aa4233-sounddevils.png"
    ["still9.png"]="/assets/95731519-6287-4bbd-a281-712ac2b13fef-still9.png"
    ["wildflower.png"]="/assets/95731519-6287-4bbd-a281-712ac2b13fef-wildflower.png"
)

for filename in "${!assets[@]}"; do
    local_path="${assets[$filename]}"
    echo "Replacing $filename..."
    find src -type f \( -name "*.md" -o -name "*.njk" -o -name "*.html" \) -exec sed -i.bak "s#https://cdn\.glitch\.[^\"]*${filename}[^\"]*#{{ \"$local_path\" | url }}#g" {} \;
done

echo "Done! Check the results with: grep -r 'assets.*png' src/"
