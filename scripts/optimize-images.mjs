import fs from 'node:fs/promises';
import path from 'node:path';
import sharp from 'sharp';

const pensDir = path.resolve('public/assets/pens');
const backupDir = path.resolve('public/assets/pens/originals');
const videoFramesDir = path.resolve('public/assets/video_frames');

async function ensureDir(dir) {
  try {
    await fs.mkdir(dir, { recursive: true });
  } catch (err) {
    if (err.code !== 'EEXIST') throw err;
  }
}

async function optimizePens() {
  console.log('\n--- 1. Otimizando imagens das Canetas (750x750 Lanczos3 / WebP & MozJPEG) ---');
  await ensureDir(backupDir);

  const files = await fs.readdir(pensDir);
  const jpgFiles = files.filter(f => f.endsWith('.jpg') && !f.startsWith('.'));

  console.log(`Encontradas ${jpgFiles.length} imagens em ${pensDir}`);

  for (const file of jpgFiles) {
    const inputPath = path.join(pensDir, file);
    const backupPath = path.join(backupDir, file);
    const baseName = path.basename(file, '.jpg');
    const webpPath = path.join(pensDir, `${baseName}.webp`);

    // Fazer backup do arquivo original se ainda não existir
    try {
      await fs.access(backupPath);
    } catch {
      await fs.copyFile(inputPath, backupPath);
      console.log(`[Backup] Salvo original: ${file}`);
    }

    const originalStats = await fs.stat(backupPath);
    const originalKB = (originalStats.size / 1024).toFixed(1);

    // Pipeline Sharp com Lanczos3, 750x750 mantendo proporção, Linear RGB / sRGB
    // fastShrinkOnLoad: false garante interpolação Lanczos3 completa em alta resolução
    const pipeline = sharp(backupPath)
      .resize({
        width: 750,
        height: 750,
        fit: 'inside', // mantém proporção
        kernel: sharp.kernel.lanczos3,
        fastShrinkOnLoad: false,
        withoutEnlargement: false,
      })
      .toColorspace('srgb');

    // 1. Gerar WebP com qualidade 85% e esforço máximo
    const webpBuffer = await pipeline
      .clone()
      .webp({
        quality: 85,
        effort: 6,
        alphaQuality: 90,
      })
      .toBuffer();

    await fs.writeFile(webpPath, webpBuffer);
    const webpKB = (webpBuffer.length / 1024).toFixed(1);

    // 2. Gerar versão MozJPEG 85% otimizada no lugar do JPG antigo (mesmo nome)
    const mozJpegBuffer = await pipeline
      .clone()
      .jpeg({
        quality: 85,
        mozjpeg: true,
        trellisQuantisation: true,
        overshootDeringing: true,
        optimizeScans: true,
      })
      .toBuffer();

    await fs.writeFile(inputPath, mozJpegBuffer);
    const mozJpegKB = (mozJpegBuffer.length / 1024).toFixed(1);

    const reductionPercent = (((originalStats.size - webpBuffer.length) / originalStats.size) * 100).toFixed(1);
    console.log(`✓ ${file}:`);
    console.log(`   Original: ${originalKB} KB -> WebP: ${webpKB} KB (-${reductionPercent}%) | MozJPEG: ${mozJpegKB} KB`);
  }
}

async function optimizeVideoFrames() {
  console.log('\n--- 2. Otimizando 192 Frames do Hero Canvas (Conversão para WebP) ---');
  const files = await fs.readdir(videoFramesDir);
  const frameFiles = files.filter(f => f.startsWith('frame_') && f.endsWith('.jpg')).sort();

  console.log(`Encontrados ${frameFiles.length} frames em ${videoFramesDir}`);

  let totalOriginal = 0;
  let totalWebp = 0;

  for (let i = 0; i < frameFiles.length; i++) {
    const file = frameFiles[i];
    const inputPath = path.join(videoFramesDir, file);
    const baseName = path.basename(file, '.jpg');
    const outputPath = path.join(videoFramesDir, `${baseName}.webp`);

    const stat = await fs.stat(inputPath);
    totalOriginal += stat.size;

    // Converter para WebP 82% com esforço 4 para renderização ultra-rápida e leve
    const webpBuffer = await sharp(inputPath)
      .webp({ quality: 82, effort: 4 })
      .toBuffer();

    totalWebp += webpBuffer.length;
    await fs.writeFile(outputPath, webpBuffer);

    if ((i + 1) % 40 === 0 || i === frameFiles.length - 1) {
      console.log(`Processados ${i + 1}/${frameFiles.length} frames...`);
    }
  }

  const origMB = (totalOriginal / (1024 * 1024)).toFixed(2);
  const webpMB = (totalWebp / (1024 * 1024)).toFixed(2);
  const savedPercent = (((totalOriginal - totalWebp) / totalOriginal) * 100).toFixed(1);

  console.log(`✓ Total Video Frames: ${origMB} MB -> ${webpMB} MB (Economia de ${savedPercent}%)`);
}

async function main() {
  try {
    const start = Date.now();
    await optimizePens();
    await optimizeVideoFrames();
    const elapsed = ((Date.now() - start) / 1000).toFixed(2);
    console.log(`\n🎉 Processamento concluído com sucesso em ${elapsed}s!\n`);
  } catch (err) {
    console.error('Erro na otimização de imagens:', err);
    process.exit(1);
  }
}

main();
