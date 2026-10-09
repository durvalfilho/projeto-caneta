import os
import subprocess
import struct
import tempfile
from pathlib import Path

WORKSPACE = Path("/Users/durvalfilho/projeto1")
SVG_PATH = WORKSPACE / "public" / "favicon.svg"
ICO_PATH = WORKSPACE / "public" / "favicon.ico"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

svg_content = SVG_PATH.read_text()

with tempfile.TemporaryDirectory() as tmpdir:
    tmpdir = Path(tmpdir)
    
    # Create HTML files for each size
    sizes = [16, 32, 48, 64]
    png_data_list = []
    
    for size in sizes:
        html_file = tmpdir / f"icon_{size}.html"
        png_file = tmpdir / f"icon_{size}.png"
        
        html_file.write_text(f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  html, body {{
    width: {size}px;
    height: {size}px;
    background: transparent;
    overflow: hidden;
  }}
  svg {{
    width: {size}px;
    height: {size}px;
    display: block;
  }}
</style>
</head>
<body>
{svg_content}
</body>
</html>""")
        
        cmd = [
            CHROME,
            "--headless",
            "--disable-gpu",
            f"--screenshot={png_file}",
            f"--window-size={size},{size}",
            f"--default-background-color=00000000",
            f"file://{html_file}"
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if not png_file.exists():
            print(f"Error generating {size}x{size}:", res.stderr)
            continue
            
        png_bytes = png_file.read_bytes()
        print(f"Generated {size}x{size}: {len(png_bytes)} bytes")
        png_data_list.append((size, png_bytes))
        
    if not png_data_list:
        raise RuntimeError("No PNGs were rendered!")
        
    # Build standard multi-resolution ICO file with embedded PNGs (supported by modern OS and browsers)
    # Header: 6 bytes
    # Reserved: 0 (2 bytes)
    # Type: 1 (2 bytes for icon)
    # Count: len(png_data_list) (2 bytes)
    header = struct.pack("<HHH", 0, 1, len(png_data_list))
    
    entries = []
    offset = 6 + 16 * len(png_data_list)
    
    for size, data in png_data_list:
        w = size if size < 256 else 0
        h = size if size < 256 else 0
        color_count = 0
        reserved = 0
        planes = 1
        bpp = 32
        data_len = len(data)
        
        entry = struct.pack("<BBBBHHII", w, h, color_count, reserved, planes, bpp, data_len, offset)
        entries.append(entry)
        offset += data_len
        
    ico_bytes = header + b"".join(entries) + b"".join([d for _, d in png_data_list])
    ICO_PATH.write_bytes(ico_bytes)
    print(f"Successfully wrote multi-resolution ICO to {ICO_PATH} ({len(ico_bytes)} bytes)")
