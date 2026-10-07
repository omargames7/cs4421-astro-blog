import type { APIRoute } from 'astro';

export const prerender = false;

export const GET: APIRoute = () =>
	Response.json({
		status: 'ready',
		timestamp: new Date().toISOString(),
	});
