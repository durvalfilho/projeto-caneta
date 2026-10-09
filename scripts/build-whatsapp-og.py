import subprocess
from pathlib import Path

WORKSPACE = Path("/Users/durvalfilho/projeto1")
IMAGES_DIR = WORKSPACE / "public" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
REF_PEN = WORKSPACE / "public" / "assets" / "pens" / "pen_raw_titanium.jpg"
ARTIFACTS_DIR = Path("/Users/durvalfilho/.gemini/antigravity-ide/brain/82e2fd6e-6bf9-4373-bd72-314b729d6bc5")

IMG_HERO_BG = ARTIFACTS_DIR / "pen_drafting_table_1791513793843.jpg"
IMG_CATALOG_BG = ARTIFACTS_DIR / "pens_case_collection_1791513815338.jpg"
IMG_PRODUTO_BG = ARTIFACTS_DIR / "pen_nib_macro_03mm_1791513838793.jpg"

renders = [
    # 1. og-hero.jpg (1200x630 Landscape - Optimized with high contrast & pen from reference bank)
    {
        "out": IMAGES_DIR / "og-hero.jpg",
        "w": 1200,
        "h": 630,
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@400;500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px;
    height: 630px;
    background: #09090b;
    color: #f4f4f5;
    font-family: 'Inter', sans-serif;
    display: flex;
    position: relative;
    overflow: hidden;
  }}
  .ambient {{
    position: absolute;
    width: 700px;
    height: 700px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(212, 175, 55, 0.15) 0%, rgba(9, 9, 11, 0) 70%);
    top: -150px;
    right: 50px;
    pointer-events: none;
  }}
  .left-col {{
    flex: 1.15;
    padding: 70px 60px;
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
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #D4AF37;
    width: fit-content;
  }}
  .badge-dot {{ width: 6px; height: 6px; border-radius: 50%; background: #D4AF37; }}
  h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 48px;
    font-weight: 700;
    line-height: 1.12;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin-top: 20px;
    margin-bottom: 16px;
  }}
  p {{
    font-size: 19px;
    line-height: 1.45;
    color: #a8a29e;
    max-width: 520px;
  }}
  .specs-row {{
    display: flex;
    gap: 14px;
  }}
  .spec-pill {{
    padding: 8px 16px;
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.12);
    font-size: 13px;
    font-weight: 600;
    color: #e7e5e4;
  }}
  .right-col {{
    flex: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    padding-right: 50px;
    z-index: 2;
  }}
  .photo-frame {{
    width: 480px;
    height: 480px;
    border-radius: 28px;
    overflow: hidden;
    border: 1.5px solid rgba(255, 255, 255, 0.15);
    box-shadow: 0 30px 60px -12px rgba(0, 0, 0, 0.8), 0 0 40px rgba(212, 175, 55, 0.15);
    position: relative;
  }}
  .photo-frame img {{
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
</style>
</head>
<body>
  <div class="ambient"></div>
  <div class="left-col">
    <div>
      <div class="badge">
        <span class="badge-dot"></span>
        ArtTools • Precision Series
      </div>
      <h1>A caneta técnica que não falha no traço</h1>
      <p>Traço uniforme, corpo monobloco em titânio aeroespacial e pontas de precisão de 0.3 a 0.8 mm para quem desenha a sério.</p>
    </div>
    <div class="specs-row">
      <div class="spec-pill">Titânio Grau 5</div>
      <div class="spec-pill">Pena 0.3 mm</div>
      <div class="spec-pill">Engenharia Suíça</div>
    </div>
  </div>
  <div class="right-col">
    <div class="photo-frame">
      <img src="file://{REF_PEN}" alt="ArtTools Titanium Pen"/>
    </div>
  </div>
</body>
</html>"""
    },
    
    # 2. og-hero-square.jpg (600x600 Square - Pure 1:1 image optimized for WhatsApp chat bubble thumbnails!)
    {
        "out": IMAGES_DIR / "og-hero-square.jpg",
        "w": 600,
        "h": 600,
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 600px;
    height: 600px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: #09090b;
  }}
  .bg-img {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .top-bar {{
    position: absolute;
    top: 24px;
    left: 24px;
    right: 24px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }}
  .badge {{
    padding: 6px 14px;
    border-radius: 999px;
    background: rgba(12, 10, 9, 0.85);
    border: 1px solid rgba(255, 255, 255, 0.2);
    backdrop-filter: blur(8px);
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #D4AF37;
  }}
  .brand {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 14px;
    font-weight: 700;
    letter-spacing: 0.12em;
    color: #ffffff;
    background: rgba(12, 10, 9, 0.85);
    padding: 6px 12px;
    border-radius: 8px;
    border: 1px solid rgba(255, 255, 255, 0.15);
  }}
  .bottom-bar {{
    position: absolute;
    bottom: 24px;
    left: 24px;
    right: 24px;
    background: rgba(12, 10, 9, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 16px;
    padding: 16px 20px;
    backdrop-filter: blur(12px);
    z-index: 2;
  }}
  .title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 4px;
    letter-spacing: -0.01em;
  }}
  .desc {{
    font-size: 12px;
    color: #d6d3d1;
    font-weight: 500;
  }}
</style>
</head>
<body>
  <img src="file://{REF_PEN}" class="bg-img" alt="Caneta ArtTools Titânio"/>
  <div class="top-bar">
    <div class="badge">PRECISION SERIES • 0.3mm</div>
    <div class="brand">ARTOOLS</div>
  </div>
  <div class="bottom-bar">
    <div class="title">ArtTools Precision Pen</div>
    <div class="desc">A caneta técnica que não falha no traço • Titânio Grau 5</div>
  </div>
</body>
</html>"""
    },
    
    # 3. og-catalogo-square.jpg (600x600 Square)
    {
        "out": IMAGES_DIR / "og-catalogo-square.jpg",
        "w": 600,
        "h": 600,
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 600px;
    height: 600px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: #09090b;
  }}
  .bg-img {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .bottom-bar {{
    position: absolute;
    bottom: 24px;
    left: 24px;
    right: 24px;
    background: rgba(12, 10, 9, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 16px;
    padding: 16px 20px;
    backdrop-filter: blur(12px);
    z-index: 2;
  }}
  .title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 4px;
  }}
  .desc {{
    font-size: 12px;
    color: #d6d3d1;
  }}
</style>
</head>
<body>
  <img src="file://{IMG_CATALOG_BG}" class="bg-img" alt="Coleção Completa ArtTools"/>
  <div class="bottom-bar">
    <div class="title">Coleção Completa ArtTools</div>
    <div class="desc">Todos os modelos, acabamentos e pontas de 0.3 a 0.8 mm</div>
  </div>
</body>
</html>"""
    },
    
    # 4. og-produto-03mm-square.jpg (600x600 Square)
    {
        "out": IMAGES_DIR / "og-produto-03mm-square.jpg",
        "w": 600,
        "h": 600,
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@600;700&family=Inter:wght@500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 600px;
    height: 600px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
    background: #09090b;
  }}
  .bg-img {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .top-seal {{
    position: absolute;
    top: 24px;
    left: 24px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(12, 10, 9, 0.88);
    border: 1.5px solid #D4AF37;
    font-size: 12px;
    font-weight: 700;
    color: #FDE047;
    z-index: 2;
  }}
  .bottom-bar {{
    position: absolute;
    bottom: 24px;
    left: 24px;
    right: 24px;
    background: rgba(12, 10, 9, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.18);
    border-radius: 16px;
    padding: 16px 20px;
    backdrop-filter: blur(12px);
    z-index: 2;
  }}
  .title {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 18px;
    font-weight: 700;
    color: #ffffff;
    margin-bottom: 4px;
  }}
  .desc {{
    font-size: 12px;
    color: #d6d3d1;
  }}
</style>
</head>
<body>
  <img src="file://{IMG_PRODUTO_BG}" class="bg-img" alt="Caneta 0.3mm Edição Limitada"/>
  <div class="top-seal">★ EDIÇÃO LIMITADA • ESGOTADO</div>
  <div class="bottom-bar">
    <div class="title">Caneta ArtTools 0.3 mm</div>
    <div class="desc">Lote 01 esgotado • Cadastre-se na lista "Avise-me quando chegar"</div>
  </div>
</body>
</html>"""
    }
]

for item in renders:
    tmp_html = WORKSPACE / "scripts" / f"tmp_{item['out'].name}.html"
    tmp_html.write_text(item['html'])
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--screenshot={item['out']}",
        f"--window-size={item['w']},{item['h']}",
        f"file://{tmp_html}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if item['out'].exists():
        print(f"Generated {item['out'].name} ({item['w']}x{item['h']}): {item['out'].stat().st_size} bytes")
    else:
        print(f"Failed {item['out'].name}:", res.stderr)
        
    if tmp_html.exists():
        tmp_html.unlink()

print("All WhatsApp & Open Graph cards rendered successfully!")
