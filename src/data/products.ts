import penRawTitanium from '../assets/pens/pen_raw_titanium.webp';
import penStealthBlack from '../assets/pens/pen_stealth_black.webp';
import penChampagneGold from '../assets/pens/pen_champagne_gold.webp';
import penMidnightBlue from '../assets/pens/pen_midnight_blue.webp';
import penForgedCarbon from '../assets/pens/pen_forged_carbon.webp';
import penSpaceSilver from '../assets/pens/pen_space_silver.webp';
import penGunmetalGray from '../assets/pens/pen_gunmetal_gray.webp';
import penObsidianCopper from '../assets/pens/pen_obsidian_copper.webp';

export interface ProductSpec {
	label: string;
	value: string;
}

export interface ProductImage {
	image: any;
	label: string;
}

export interface Product {
	id: string;
	slug: string;
	title: string;
	seoTitle?: string;
	seoDescription?: string;
	reference: string;
	series: string;
	badgeLeft?: string;
	badgeRight?: string;
	image: any;
	images?: ProductImage[];
	description: string;
	specs: ProductSpec[];
	pena: string;
	material: string;
	recarga: string;
}

export const products: Product[] = [
	{
		id: '01',
		slug: 'arttools-03mm',
		title: 'Caneta ArtTools 0.3 mm — Titanium Stealth',
		seoTitle: 'Caneta ArtTools 0.3 mm — Edição Limitada | Avise-me quando chegar',
		seoDescription:
			'A ArtTools 0.3 mm está esgotada. Cadastre seu e-mail e seja o primeiro a saber da reposição.',
		reference: 'REF. AR-TS01',
		series: 'Precision Series • 01',
		badgeLeft: 'EDIÇÃO LIMITADA',
		badgeRight: 'ESGOTADO',
		image: penRawTitanium,
		images: [
			{ image: penRawTitanium, label: 'Visão Geral' },
			{ image: penStealthBlack, label: 'Empunhadura Laser' },
			{ image: penSpaceSilver, label: 'Ponta & Rolamento' },
			{ image: penForgedCarbon, label: 'Chassi & Acabamento' },
		],
		description:
			'Design ultra-leve de precisão usinado em titânio aeroespacial Grau 5 com equilíbrio de peso milimétrico. Forjada a partir de uma barra sólida de Titânio Ti-6Al-4V usinada em CNC de 5 eixos para eliminar qualquer micro-vibração durante a escrita.',
		specs: [
			{ label: 'PENA', value: 'Ouro 18k Fine (0.3 mm)' },
			{ label: 'MATERIAL', value: 'Titânio Ti-6Al-4V (Grau 5)' },
			{ label: 'PESO', value: '14.0 g (Equilíbrio 50/50)' },
			{ label: 'RECARGA', value: 'Tinteiro / Pistão' },
			{ label: 'MECANISMO', value: 'Silent-Click Amortecido' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: 'Ouro 18k Fine (0.3 mm)',
		material: 'Titânio G5',
		recarga: 'Tinteiro / Pistão',
	},
	{
		id: '02',
		slug: 'precision-ceramic-white',
		title: 'Precision Ceramic White',
		reference: 'REF. AR-CW02',
		series: 'Ceramic Series • 02',
		badgeLeft: 'NOVO LANÇAMENTO',
		badgeRight: 'EM BREVE',
		image: penStealthBlack,
		images: [
			{ image: penStealthBlack, label: 'Visão Geral' },
			{ image: penSpaceSilver, label: 'Chassi' },
			{ image: penRawTitanium, label: 'Detalhes' },
		],
		description:
			'Revestimento cerâmico de alta resistência com acabamento fosco aveludado e mecanismo retrátil hidráulico.',
		specs: [
			{ label: 'PENA', value: 'Aço Inox M (0.5 mm)' },
			{ label: 'MATERIAL', value: 'Cerâmica Zircônia' },
			{ label: 'PESO', value: '16.5 g' },
			{ label: 'RECARGA', value: 'Rollerball G2' },
			{ label: 'MECANISMO', value: 'Retrátil Hidráulico' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: 'Aço Inox M',
		material: 'Cerâmica Zircônia',
		recarga: 'Rollerball G2',
	},
	{
		id: '03',
		slug: 'obsidian-matte-black',
		title: 'Obsidian Matte Black',
		reference: 'REF. AR-MB03',
		series: 'Studio Series • 03',
		badgeLeft: 'COLEÇÃO 2026',
		badgeRight: 'ESGOTADO',
		image: penChampagneGold,
		images: [
			{ image: penChampagneGold, label: 'Visão Geral' },
			{ image: penStealthBlack, label: 'Grip' },
		],
		description:
			'Acabamento obsidian antirreflexo com gravura a laser e sistema de amortecimento tátil ao escrever.',
		specs: [
			{ label: 'PENA', value: 'Carbon EF (0.38 mm)' },
			{ label: 'MATERIAL', value: 'Alumínio Anodizado' },
			{ label: 'PESO', value: '13.5 g' },
			{ label: 'RECARGA', value: 'Esferográfica' },
			{ label: 'MECANISMO', value: 'Twist Rotativo' },
			{ label: 'TOLERÂNCIA', value: '± 0.008 mm' },
		],
		pena: 'Carbon EF',
		material: 'Alumínio Anodizado',
		recarga: 'Esferográfica',
	},
	{
		id: '04',
		slug: 'precision-midnight-navy',
		title: 'Precision Midnight Navy',
		reference: 'REF. AR-MN04',
		series: 'Atelier Series • 04',
		badgeLeft: 'ATELIER SERIES',
		badgeRight: 'EM BREVE',
		image: penMidnightBlue,
		images: [
			{ image: penMidnightBlue, label: 'Visão Geral' },
			{ image: penSpaceSilver, label: 'Ponta' },
		],
		description:
			'Pigmentação eletroquímica azul profunda com clip negro PVD e mecanismo de amortecimento silencioso.',
		specs: [
			{ label: 'PENA', value: '0.3 mm Fine' },
			{ label: 'MATERIAL', value: 'Alumínio 6061' },
			{ label: 'PESO', value: '14.2 g' },
			{ label: 'RECARGA', value: 'Rollerball G2' },
			{ label: 'MECANISMO', value: 'Silent-Click' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: '0.3 mm Fine',
		material: 'Alumínio 6061',
		recarga: 'Rollerball G2',
	},
	{
		id: '05',
		slug: 'champagne-brass-heritage',
		title: 'Champagne Brass Heritage',
		reference: 'REF. AR-BH05',
		series: 'Heritage Line • 05',
		badgeLeft: 'HERITAGE LINE',
		badgeRight: 'PRÉ-VENDA',
		image: penChampagneGold,
		images: [
			{ image: penChampagneGold, label: 'Visão Geral' },
			{ image: penRawTitanium, label: 'Pátina' },
		],
		description:
			'Corpo em liga nobre de latão náutico escovado manualmente com pátina que evolui ao longo do tempo.',
		specs: [
			{ label: 'PENA', value: 'Ouro 14k M' },
			{ label: 'MATERIAL', value: 'Latão Escovado' },
			{ label: 'PESO', value: '28.0 g' },
			{ label: 'RECARGA', value: 'Tinteiro / Conversor' },
			{ label: 'MECANISMO', value: 'Rosca Magnética' },
			{ label: 'TOLERÂNCIA', value: '± 0.010 mm' },
		],
		pena: 'Ouro 14k M',
		material: 'Latão Escovado',
		recarga: 'Tinteiro / Conversor',
	},
	{
		id: '06',
		slug: 'forged-carbon-hypercraft',
		title: 'Forged Carbon Hypercraft',
		reference: 'REF. AR-FC06',
		series: 'Hypercraft • 06',
		badgeLeft: 'HYPERCRAFT',
		badgeRight: 'ESGOTADO',
		image: penForgedCarbon,
		images: [
			{ image: penForgedCarbon, label: 'Visão Geral' },
			{ image: penStealthBlack, label: 'Fibra' },
		],
		description:
			'Fibras de carbono forjadas a alta pressão com conexões usinadas em titânio. Estrutura ultra-leve de 11.8g.',
		specs: [
			{ label: 'PENA', value: 'Carbon 0.3mm' },
			{ label: 'MATERIAL', value: 'Carbono Forjado' },
			{ label: 'PESO', value: '11.8 g' },
			{ label: 'RECARGA', value: 'Rollerball G2' },
			{ label: 'MECANISMO', value: 'Mecanismo de Esfera' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: 'Carbon 0.3mm',
		material: 'Carbono Forjado',
		recarga: 'Rollerball G2',
	},
	{
		id: '07',
		slug: 'space-silver-monobloc',
		title: 'Space Silver Monobloc',
		reference: 'REF. AR-SS07',
		series: 'Precision Series • 07',
		badgeLeft: 'PRECISION SERIES',
		badgeRight: 'EM BREVE',
		image: penSpaceSilver,
		images: [
			{ image: penSpaceSilver, label: 'Visão Geral' },
			{ image: penRawTitanium, label: 'Ponta' },
		],
		description:
			'Acabamento prateado com polimento micro-esferado e sistema de tinta híbrida com regulação capilar.',
		specs: [
			{ label: 'PENA', value: 'Aço Inox F' },
			{ label: 'MATERIAL', value: 'Alumínio 6061' },
			{ label: 'PESO', value: '13.9 g' },
			{ label: 'RECARGA', value: 'Rollerball G2' },
			{ label: 'MECANISMO', value: 'Silent-Click' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: 'Aço Inox F',
		material: 'Alumínio 6061',
		recarga: 'Rollerball G2',
	},
	{
		id: '08',
		slug: 'gunmetal-dark-technical',
		title: 'Gunmetal Dark Technical',
		reference: 'REF. AR-GT08',
		series: 'Studio Edition • 08',
		badgeLeft: 'STUDIO EDITION',
		badgeRight: 'PRÉ-VENDA',
		image: penGunmetalGray,
		images: [
			{ image: penGunmetalGray, label: 'Visão Geral' },
			{ image: penStealthBlack, label: 'Grafite' },
		],
		description:
			'Tratamento em grafite escuro com micro-ranhuras lineares para traço milimétrico e estabilidade absoluta.',
		specs: [
			{ label: 'PENA', value: '0.5 mm Medium' },
			{ label: 'MATERIAL', value: 'Alu Anodizado' },
			{ label: 'PESO', value: '14.5 g' },
			{ label: 'RECARGA', value: 'Esferográfica' },
			{ label: 'MECANISMO', value: 'Click Duplo' },
			{ label: 'TOLERÂNCIA', value: '± 0.006 mm' },
		],
		pena: '0.5 mm Medium',
		material: 'Alu Anodizado',
		recarga: 'Esferográfica',
	},
	{
		id: '09',
		slug: 'obsidian-copper-artisan',
		title: 'Obsidian Copper Artisan',
		reference: 'REF. AR-CA09',
		series: 'Artisan Edition • 09',
		badgeLeft: 'EDIÇÃO LIMITADA',
		badgeRight: 'EM BREVE',
		image: penObsidianCopper,
		images: [
			{ image: penObsidianCopper, label: 'Visão Geral' },
			{ image: penChampagneGold, label: 'Cobre' },
		],
		description:
			'Seção de pega em cobre de alta densidade combinada com chassi escurecido por deposição física de vapor (DLC).',
		specs: [
			{ label: 'PENA', value: 'Tungstênio 0.3' },
			{ label: 'MATERIAL', value: 'Cobre + DLC' },
			{ label: 'PESO', value: '22.0 g' },
			{ label: 'RECARGA', value: 'Rollerball G2' },
			{ label: 'MECANISMO', value: 'Retrátil' },
			{ label: 'TOLERÂNCIA', value: '± 0.005 mm' },
		],
		pena: 'Tungstênio 0.3',
		material: 'Cobre + DLC',
		recarga: 'Rollerball G2',
	},
];
