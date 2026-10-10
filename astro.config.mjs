// @ts-check
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite';
import sitemap from '@astrojs/sitemap';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

import vercel from '@astrojs/vercel';

// https://astro.build/config
export default defineConfig({
	site: 'https://projeto-caneta-gamma.vercel.app',
	adapter: vercel(),
	integrations: [
		sitemap({
			changefreq: 'weekly',
			priority: 0.7,
			lastmod: new Date(),
			serialize(item) {
				if (item.url === 'https://projeto-caneta-gamma.vercel.app/') {
					item.changefreq = 'daily';
					item.priority = 1.0;
				} else if (item.url.includes('/catalogo')) {
					item.changefreq = 'weekly';
					item.priority = 0.9;
				} else if (item.url.includes('/produtos/arttools-03mm')) {
					item.changefreq = 'weekly';
					item.priority = 0.9;
				} else if (item.url.includes('/produtos/')) {
					item.changefreq = 'weekly';
					item.priority = 0.8;
				}
				return item;
			},
		}),
		{
			name: 'sitemap-xml-fallback',
			hooks: {
				'astro:build:done': async ({ dir }) => {
					const targetDir = fileURLToPath(dir);
					const indexXml = path.join(targetDir, 'sitemap-index.xml');
					const rootXml = path.join(targetDir, 'sitemap.xml');
					if (fs.existsSync(indexXml)) {
						fs.copyFileSync(indexXml, rootXml);
					}
				},
			},
		},
	],
	prefetch: false,
	build: {
		inlineStylesheets: 'always',
	},
	vite: {
		plugins: [tailwindcss()],
	},
});
