import type { APIRoute } from 'astro';
import crypto from 'node:crypto';

export const prerender = false;

function hashSha256(value: string): string {
	return crypto.createHash('sha256').update(value.trim().toLowerCase()).digest('hex');
}

function normalizeAndHashPhone(phone: string): string {
	let digits = phone.replace(/\D/g, '');
	// Se for número brasileiro sem DDI (10 ou 11 dígitos), adiciona 55
	if (digits.length === 10 || digits.length === 11) {
		digits = '55' + digits;
	}
	return crypto.createHash('sha256').update(digits).digest('hex');
}

export const POST: APIRoute = async ({ request }) => {
	try {
		const data = await request.json();
		const { name, email, phone, productName, productSlug, eventId, testEventCode } = data;

		if (!email) {
			return new Response(JSON.stringify({ error: 'E-mail é obrigatório' }), {
				status: 400,
				headers: { 'Content-Type': 'application/json' },
			});
		}

		const pixelId = process.env.META_PIXEL_ID || import.meta.env.META_PIXEL_ID || '1105988018496370';
		const accessToken =
			process.env.META_ACCESS_TOKEN ||
			import.meta.env.META_ACCESS_TOKEN ||
			'EAADx3RBIacgBSg6lHsJOeblzihcVUyS99ZB7dAzkryyhKWSbGaQyievHLdoszZBgThvP8iJfPN1SpjFHGGbSU0mvDJ2VPXN7xBlDttw9RKbFEus4N9bU4LaWJ7NfQFbf5ECFloIkpIhuk8PhOhAG5lOC9MCDmZAZCEN0PlkXHQkBNWZAOiJelMC0hPpy22AZDZD';

		// Obter IP e User-Agent do visitante
		const clientIp =
			request.headers.get('x-forwarded-for')?.split(',')[0].trim() ||
			request.headers.get('x-real-ip') ||
			'127.0.0.1';
		const clientUserAgent = request.headers.get('user-agent') || 'Mozilla/5.0';

		const userData: Record<string, any> = {
			em: [hashSha256(email)],
			client_ip_address: clientIp,
			client_user_agent: clientUserAgent,
		};

		if (phone && typeof phone === 'string' && phone.trim()) {
			userData.ph = [normalizeAndHashPhone(phone)];
		}

		if (name && typeof name === 'string' && name.trim()) {
			const firstName = name.trim().split(' ')[0];
			userData.fn = [hashSha256(firstName)];
		}

		const generatedEventId =
			eventId || `lead_${Date.now()}_${Math.random().toString(36).substring(2, 9)}`;

		const payload: Record<string, any> = {
			data: [
				{
					event_name: 'Lead',
					event_time: Math.floor(Date.now() / 1000),
					event_id: generatedEventId,
					action_source: 'website',
					event_source_url:
						request.headers.get('referer') ||
						'https://projeto-caneta-gamma.vercel.app/produtos/arttools-03mm',
					user_data: userData,
					custom_data: {
						content_name: productName || 'Caneta ArtTools',
						content_category: 'Canetas Técnicas',
						content_ids: productSlug ? [productSlug] : undefined,
					},
				},
			],
			access_token: accessToken,
		};

		if (testEventCode || process.env.META_TEST_EVENT_CODE) {
			payload.test_event_code = testEventCode || process.env.META_TEST_EVENT_CODE;
		}

		const response = await fetch(`https://graph.facebook.com/v21.0/${pixelId}/events`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(payload),
		});

		const result = await response.json();

		return new Response(JSON.stringify({ success: true, eventId: generatedEventId, meta: result }), {
			status: 200,
			headers: { 'Content-Type': 'application/json' },
		});
	} catch (err: any) {
		console.error('Erro ao enviar lead para a Meta Conversions API:', err);
		return new Response(JSON.stringify({ error: err.message || 'Erro interno' }), {
			status: 500,
			headers: { 'Content-Type': 'application/json' },
		});
	}
};
