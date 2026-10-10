import crypto from 'node:crypto';

function hashSha256(value) {
	return crypto.createHash('sha256').update(value.trim().toLowerCase()).digest('hex');
}

function normalizeAndHashPhone(phone) {
	let digits = phone.replace(/\D/g, '');
	if (digits.length === 10 || digits.length === 11) {
		digits = '55' + digits;
	}
	return crypto.createHash('sha256').update(digits).digest('hex');
}

export default async function handler(req, res) {
	if (req.method !== 'POST') {
		return res.status(405).json({ error: 'Method not allowed' });
	}

	try {
		const body = typeof req.body === 'string' ? JSON.parse(req.body) : req.body || {};
		const { name, email, phone, productName, productSlug, eventId, testEventCode } = body;

		if (!email) {
			return res.status(400).json({ error: 'E-mail é obrigatório' });
		}

		const pixelId = process.env.META_PIXEL_ID || '1105988018496370';
		const accessToken =
			process.env.META_ACCESS_TOKEN ||
			'EAADx3RBIacgBSg6lHsJOeblzihcVUyS99ZB7dAzkryyhKWSbGaQyievHLdoszZBgThvP8iJfPN1SpjFHGGbSU0mvDJ2VPXN7xBlDttw9RKbFEus4N9bU4LaWJ7NfQFbf5ECFloIkpIhuk8PhOhAG5lOC9MCDmZAZCEN0PlkXHQkBNWZAOiJelMC0hPpy22AZDZD';

		const clientIp =
			(req.headers['x-forwarded-for'] || '').split(',')[0].trim() ||
			req.headers['x-real-ip'] ||
			'127.0.0.1';
		const clientUserAgent = req.headers['user-agent'] || 'Mozilla/5.0';

		const userData = {
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

		const payload = {
			data: [
				{
					event_name: 'Lead',
					event_time: Math.floor(Date.now() / 1000),
					event_id: generatedEventId,
					action_source: 'website',
					event_source_url:
						req.headers['referer'] ||
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

		const fbResponse = await fetch(`https://graph.facebook.com/v21.0/${pixelId}/events`, {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(payload),
		});

		const result = await fbResponse.json();

		return res.status(200).json({ success: true, eventId: generatedEventId, meta: result });
	} catch (err) {
		console.error('Erro CAPI:', err);
		return res.status(500).json({ error: err.message || 'Erro interno' });
	}
}
