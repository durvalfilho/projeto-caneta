import subprocess
from pathlib import Path

WORKSPACE = Path("/Users/durvalfilho/projeto1")
IMAGES_DIR = WORKSPACE / "public" / "images"
IMAGES_DIR.mkdir(parents=True, exist_ok=True)

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
ARTIFACTS_DIR = Path("/Users/durvalfilho/.gemini/antigravity-ide/brain/82e2fd6e-6bf9-4373-bd72-314b729d6bc5")

IMG_HERO = ARTIFACTS_DIR / "pen_drafting_table_1791513793843.jpg"
IMG_CATALOG = ARTIFACTS_DIR / "pens_case_collection_1791513815338.jpg"
IMG_PRODUTO = ARTIFACTS_DIR / "pen_nib_macro_03mm_1791513838793.jpg"

cards = [
    {
        "name": "og-hero.jpg",
        "bg": str(IMG_HERO),
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px;
    height: 630px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
  }}
  .bg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(12, 10, 9, 0.92) 0%, rgba(12, 10, 9, 0.75) 45%, rgba(12, 10, 9, 0.15) 100%);
  }}
  .content {{
    position: relative;
    z-index: 2;
    height: 100%;
    width: 680px;
    padding: 70px 60px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(10px);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #f5f5f4;
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
    color: #d6d3d1;
  }}
  .footer-tags {{
    display: flex;
    gap: 16px;
  }}
  .tag {{
    padding: 6px 14px;
    background: rgba(0, 0, 0, 0.6);
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 8px;
    font-size: 13px;
    font-weight: 500;
    color: #a8a29e;
  }}
</style>
</head>
<body>
  <img src="file://{IMG_HERO}" class="bg" alt="Hero Background"/>
  <div class="overlay"></div>
  <div class="content">
    <div>
      <div class="badge">
        <span class="badge-dot"></span>
        ArtTools • Bancada de Desenho
      </div>
      <h1>A caneta técnica que não falha no traço</h1>
      <p>Traço uniforme, corpo em titânio e pontas de 0.3 a 0.8 mm para ilustradores e designers que exigem precisão absoluta.</p>
    </div>
    <div class="footer-tags">
      <span class="tag">Traço Constante</span>
      <span class="tag">Corpo Monobloco</span>
      <span class="tag">Engenharia Suíça</span>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "name": "og-catalogo.jpg",
        "bg": str(IMG_CATALOG),
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px;
    height: 630px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
  }}
  .bg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(12, 10, 9, 0.85) 0%, rgba(12, 10, 9, 0.4) 40%, rgba(12, 10, 9, 0.88) 100%);
  }}
  .header {{
    position: absolute;
    top: 50px;
    left: 60px;
    right: 60px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }}
  .badge {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    backdrop-filter: blur(12px);
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #f5f5f4;
  }}
  .badge-dot {{ width: 6px; height: 6px; border-radius: 50%; background: #D4AF37; }}
  .bottom-card {{
    position: absolute;
    bottom: 50px;
    left: 60px;
    right: 60px;
    background: rgba(18, 16, 15, 0.88);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 20px;
    padding: 28px 40px;
    backdrop-filter: blur(16px);
    display: flex;
    justify-content: space-between;
    align-items: center;
    z-index: 2;
  }}
  h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 34px;
    font-weight: 700;
    color: #ffffff;
    letter-spacing: -0.02em;
    margin-bottom: 6px;
  }}
  p {{
    font-size: 16px;
    color: #a8a29e;
  }}
  .specs-pills {{
    display: flex;
    gap: 12px;
  }}
  .pill {{
    padding: 8px 18px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.06);
    border: 1px solid rgba(255, 255, 255, 0.1);
    font-size: 13px;
    font-weight: 600;
    color: #e7e5e4;
  }}
</style>
</head>
<body>
  <img src="file://{IMG_CATALOG}" class="bg" alt="Catalog Case"/>
  <div class="overlay"></div>
  <div class="header">
    <div class="badge">
      <span class="badge-dot"></span>
      Coleção Completa ArtTools
    </div>
    <div style="font-family:'Space Grotesk',sans-serif; font-weight:700; font-size:18px; letter-spacing:0.1em; color:#fff;">ARTOOLS</div>
  </div>
  <div class="bottom-card">
    <div>
      <h1>Coleção completa ArtTools — Todos os modelos e pontas</h1>
      <p>Veja todas as espessuras de ponta (0.3 a 0.8 mm), acabamentos nobres e edições exclusivas.</p>
    </div>
    <div class="specs-pills">
      <div class="pill">5 Acabamentos</div>
      <div class="pill">Estojo CNC</div>
    </div>
  </div>
</body>
</html>"""
    },
    {
        "name": "og-produto-03mm.jpg",
        "bg": str(IMG_PRODUTO),
        "html": f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&family=Inter:wght@400;500;600&display=swap');
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    width: 1200px;
    height: 630px;
    position: relative;
    overflow: hidden;
    font-family: 'Inter', sans-serif;
  }}
  .bg {{
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }}
  .overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(90deg, rgba(12, 10, 9, 0.92) 0%, rgba(12, 10, 9, 0.72) 48%, rgba(12, 10, 9, 0.1) 100%);
  }}
  .content {{
    position: relative;
    z-index: 2;
    height: 100%;
    width: 660px;
    padding: 70px 60px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
  }}
  .badges-row {{
    display: flex;
    gap: 12px;
    align-items: center;
  }}
  .seal-limited {{
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 9px 20px;
    border-radius: 999px;
    background: linear-gradient(135deg, rgba(212, 175, 55, 0.25) 0%, rgba(180, 83, 9, 0.25) 100%);
    border: 1.5px solid #D4AF37;
    backdrop-filter: blur(12px);
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #FDE047;
    box-shadow: 0 4px 20px rgba(212, 175, 55, 0.2);
  }}
  .badge-soldout {{
    padding: 8px 16px;
    border-radius: 999px;
    background: rgba(255, 255, 255, 0.08);
    border: 1px solid rgba(255, 255, 255, 0.15);
    font-size: 12px;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: #a8a29e;
  }}
  h1 {{
    font-family: 'Space Grotesk', sans-serif;
    font-size: 46px;
    font-weight: 700;
    line-height: 1.15;
    letter-spacing: -0.03em;
    color: #ffffff;
    margin-top: 20px;
    margin-bottom: 16px;
  }}
  p {{
    font-size: 19px;
    line-height: 1.45;
    color: #d6d3d1;
  }}
  .notify-box {{
    background: rgba(28, 25, 23, 0.8);
    border: 1px solid rgba(255, 255, 255, 0.15);
    border-radius: 14px;
    padding: 16px 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: fit-content;
    gap: 20px;
  }}
  .notify-text {{
    font-size: 14px;
    color: #e7e5e4;
    font-weight: 500;
  }}
  .notify-tag {{
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #D4AF37;
    background: rgba(212, 175, 55, 0.15);
    padding: 5px 12px;
    border-radius: 6px;
  }}
</style>
</head>
<body>
  <img src="file://{IMG_PRODUTO}" class="bg" alt="Macro Nib 0.3mm"/>
  <div class="overlay"></div>
  <div class="content">
    <div>
      <div class="badges-row">
        <div class="seal-limited">
          ★ EDIÇÃO LIMITADA
        </div>
        <div class="badge-soldout">
          LOTE 01 ESGOTADO
        </div>
      </div>
      <h1>Caneta ArtTools 0.3 mm</h1>
      <p>A ArtTools 0.3 mm com pena ouro 18k e corpo em titânio Grau 5 está esgotada. Cadastre seu e-mail e seja o primeiro a saber da reposição.</p>
    </div>
    <div class="notify-box">
      <span class="notify-text">Lista de Espera Prioritária</span>
      <span class="notify-tag">Avise-me quando chegar</span>
    </div>
  </div>
</body>
</html>"""
    }
]

for card in cards:
    html_path = WORKSPACE / "scripts" / f"tmp_{card['name']}.html"
    out_path = IMAGES_DIR / card['name']
    html_path.write_text(card['html'])
    
    cmd = [
        CHROME,
        "--headless",
        "--disable-gpu",
        f"--screenshot={out_path}",
        "--window-size=1200,630",
        f"file://{html_path}"
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if out_path.exists():
        print(f"Generated {out_path.name}: {out_path.stat().st_size} bytes")
    else:
        print(f"Failed {card['name']}:", res.stderr)
        
    if html_path.exists():
        html_path.unlink()

print("All Open Graph cards built successfully!")
