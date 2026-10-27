import os
import sys
import subprocess
from styles import CSS_CONTENT
from body import BODY_CONTENT
from scripts import JS_CONTENT

sys.stdout.reconfigure(encoding='utf-8')

print("Assembling template.html...")

template_html = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>__APP_TITLE__</title>
<meta name="description" content="__APP_DESCRIPTION__">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Playfair+Display:ital,wght@0,600;0,700;1,400&display=swap" rel="stylesheet">
<style>
{CSS_CONTENT}
</style>
</head>
<body>
{BODY_CONTENT}

<script>
{JS_CONTENT}
</script>
</body>
</html>
"""

with open('template.html', 'w', encoding='utf-8') as f:
    f.write(template_html)

print(f"template.html created successfully ({len(template_html)} chars).")

# Now run assemble.py to produce index.html
print("Running assemble.py...")
import assemble
assemble.assemble()

print("Verifying index.html...")
if not os.path.exists('index.html'):
    print("Error: index.html was not generated!")
    sys.exit(1)

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract script to check with node
script_start = idx_content.find('<script>')
script_end = idx_content.rfind('</script>')
if script_start != -1 and script_end != -1:
    js_code = idx_content[script_start+8:script_end]
    temp_js_path = 'temp_check.js'
    with open(temp_js_path, 'w', encoding='utf-8') as f_js:
        f_js.write(js_code)
    
    print("Testing JavaScript syntax with Node.js...")
    res = subprocess.run(['node', '-c', temp_js_path], capture_output=True, text=True)
    if res.returncode == 0:
        print("✓ JavaScript syntax validation PASSED!")
        os.remove(temp_js_path)
    else:
        print("✗ JavaScript syntax error found:")
        print(res.stderr)
        sys.exit(1)

print("Done! DeutschMeister successfully built.")
