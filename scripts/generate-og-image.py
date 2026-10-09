import subprocess
import os
from pathlib import Path

WORKSPACE = Path("/Users/durvalfilho/projeto1")
IMAGES_DIR = WORKSPACE / "public" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PEN_IMAGE = WORKSPACE / "public" / "assets" / "pens" / "pen_raw_titanium.jpg"
HTML_TMP = WORKSPACE / "scripts" / "og_template.html"
OUT_JPG = IMAGES_DIR / "og-default.jpg"

html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');
  
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px;
    height: 630px;
    background: #09090b;
    font-family: 'Inter', sans-serif;
    color: #f4f4f5;
    display: flex;
    position: relative;
    overflow: hidden;
  }}
  
  /* Ambient gradient background */
  .bg-glow {{
    position: absolute;
    width: 800px;
    height: 800px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(212, 175, 55, 0.12) 0%, rgba(9, 9, 11, 0) 70%);
    top: -200px;
    right: -100px;
    pointer-events: none;
  }}

  .content {{
    flex: 1.2;
    padding: 80px 70px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    z-index: 2;
  }}

  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 9999px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #d4af37;
    width: fit-content;
  }}

  .dot {{
    width: 6px;
    height: 6px;
    border-radius: 50%;
    background: #d4af37;
  }}

  h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 52px;
    font-weight: 700;
    line-height: 1.1;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin-top: 24px;
    margin-bottom: 20px;
  }}

  p {{
    font-size: 20px;
    line-height: 1.5;
    color: #a1a1aa;
    max-width: 580px;
  }}

  .specs-bar {{
    display: flex;
    gap: 28px;
    padding-top: 32px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
  }}

  .spec-item {{
    display: flex;
    flex-direction: column;
    gap: 4px;
  }}

  .spec-label {{
    font-size: 11px;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #71717a;
  }}

  .spec-val {{
    font-size: 16px;
    font-weight: 600;
    color: #f4f4f5;
  }}

  .media-col {{
    flex: 1;
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    z-index: 1;
    overflow: hidden;
  }}

  .pen-photo {{
    width: 540px;
    height: 540px;
    object-fit: cover;
    border-radius: 32px;
    border: 1px solid rgba(255, 255, 255, 0.12);
    box-shadow: 0 25px 50px -12px rgba(0, 0, 0, 0.7);
    transform: rotate(3deg);
  }}
</style>
</head>
<body>
  <div class="bg-glow"></div>
  
  <div class="content">
    <div>
      <div class="badge">
        <span class="dot"></span>
        ArtTools • Precision Series
      </div>
      <h1>Canetas técnicas para quem desenha a sério</h1>
      <p>Precisão cirúrgica de 0.3mm, titânio aeroespacial Grau 5 e fluxo contínuo para ilustradores e designers.</p>
    </div>

    <div class="specs-bar">
      <div class="spec-item">
        <span class="spec-label">Material</span>
        <span class="spec-val">Titânio Ti-6Al-4V</span>
      </div>
      <div class="spec-item">
        <span class="spec-label">Pena</span>
        <span class="spec-val">Ouro 18k Fine (0.3mm)</span>
      </div>
      <div class="spec-item">
        <span class="spec-label">Engenharia</span>
        <span class="spec-val">CNC 5 Eixos ±0.005mm</span>
      </div>
    </div>
  </div>

  <div class="media-col">
    <img src="file://{PEN_IMAGE}" class="pen-photo" alt="ArtTools Precision Pen" />
  </div>
</body>
</html>"""

HTML_TMP.write_text(html_content)

cmd = [
    CHROME,
    "--headless",
    "--disable-gpu",
    f"--screenshot={OUT_JPG}",
    "--window-size=1200,630",
    f"file://{HTML_TMP}"
]

res = subprocess.run(cmd, capture_output=True, text=True)
if OUT_JPG.exists():
    print(f"Generated {OUT_JPG}: {OUT_JPG.stat().st_size} bytes")
else:
    print("Error:", res.stderr)

if HTML_TMP.exists():
    HTML_TMP.unlink()
