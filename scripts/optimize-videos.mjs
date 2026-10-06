import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';
import ffmpegPath from 'ffmpeg-static';

const TARGET_DIRS = [
  path.resolve('public/assets/raw_files'),
  path.resolve('src/assets/raw_files'),
];

async function ensureDir(dir) {
  try {
    await fs.mkdir(dir, { recursive: true });
  } catch (err) {
    if (err.code !== 'EEXIST') throw err;
  }
}

function runFfmpeg(args) {
  return new Promise((resolve, reject) => {
    const proc = spawn(ffmpegPath, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let stderr = '';
    proc.stderr.on('data', (data) => {
      stderr += data.toString();
    });
    proc.on('close', (code) => {
      if (code === 0) {
        resolve();
      } else {
        reject(new Error(`FFmpeg exited with code ${code}:\n${stderr}`));
      }
    });
  });
}

async function optimizeVideo(videoPath, backupDir) {
  const fileName = path.basename(videoPath);
  const backupPath = path.join(backupDir, fileName);

  // 1. Fazer backup do vídeo original se ainda não existir
  try {
    await fs.access(backupPath);
  } catch {
    await fs.copyFile(videoPath, backupPath);
    console.log(`[Backup] Original salvo em: ${backupPath}`);
  }

  const statBefore = await fs.stat(backupPath);
  const sizeBeforeMB = (statBefore.size / (1024 * 1024)).toFixed(2);

  const tempOutputPath = `${videoPath}.tmp.mp4`;

  // 2. Executar compressão com H.264 1920x1080, CRF 29, Preset medium, Faststart, AAC
  // Resolução: 1920, Qualidade CRF 29, Preset medium-balanced, MP4
  const args = [
    '-y',
    '-i', backupPath,
    '-vf', 'scale=1920:-2',
    '-c:v', 'libx264',
    '-crf', '29',
    '-preset', 'medium',
    '-pix_fmt', 'yuv420p',
    '-movflags', '+faststart',
    '-c:a', 'aac',
    '-b:a', '128k',
    tempOutputPath,
  ];

  await runFfmpeg(args);

  const statAfter = await fs.stat(tempOutputPath);
  const sizeAfterMB = (statAfter.size / (1024 * 1024)).toFixed(2);
  const reductionPercent = (((statBefore.size - statAfter.size) / statBefore.size) * 100).toFixed(1);

  // Substituir com o arquivo otimizado
  await fs.rename(tempOutputPath, videoPath);

  console.log(`✓ ${fileName} (${path.dirname(videoPath).split('/').slice(-2).join('/')}):`);
  console.log(`   Original: ${sizeBeforeMB} MB -> Otimizado: ${sizeAfterMB} MB (-${reductionPercent}%)`);
  console.log(`   Config: 1920p | CRF 29 | Preset medium | faststart habilitado\n`);

  return {
    file: fileName,
    originalBytes: statBefore.size,
    optimizedBytes: statAfter.size,
  };
}

async function main() {
  console.log('====================================================');
  console.log('   Otimização de Vídeos (1920 Quality 29 Preset Medium)   ');
  console.log('====================================================\n');

  if (!ffmpegPath) {
    throw new Error('ffmpeg-static não foi encontrado.');
  }

  const start = Date.now();
  let totalOriginal = 0;
  let totalOptimized = 0;

  for (const dir of TARGET_DIRS) {
    try {
      await fs.access(dir);
    } catch {
      continue;
    }

    const backupDir = path.join(dir, 'originals');
    await ensureDir(backupDir);

    const files = await fs.readdir(dir);
    const videoFiles = files.filter(f => f.endsWith('.mp4') && !f.startsWith('.'));

    for (const file of videoFiles) {
      const fullPath = path.join(dir, file);
      const res = await optimizeVideo(fullPath, backupDir);
      totalOriginal += res.originalBytes;
      totalOptimized += res.optimizedBytes;
    }
  }

  const origMB = (totalOriginal / (1024 * 1024)).toFixed(2);
  const optMB = (totalOptimized / (1024 * 1024)).toFixed(2);
  const saved = (((totalOriginal - totalOptimized) / totalOriginal) * 100).toFixed(1);
  const elapsed = ((Date.now() - start) / 1000).toFixed(2);

  console.log(`🎉 Concluído com sucesso em ${elapsed}s!`);
  console.log(`📊 Total: ${origMB} MB -> ${optMB} MB (Economia global de ${saved}%)\n`);
}

main().catch((err) => {
  console.error('Erro na otimização de vídeos:', err);
  process.exit(1);
});
