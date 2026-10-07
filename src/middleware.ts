import { defineMiddleware } from 'astro:middleware';

export const onRequest = defineMiddleware(async (context, next) => {
	const startedAt = performance.now();
	let statusCode = 500;

	try {
		const response = await next();
		statusCode = response.status;
		return response;
	} finally {
		const logEntry = {
			timestamp: new Date().toISOString(),
			level: statusCode >= 500 ? 'ERROR' : statusCode >= 400 ? 'WARN' : 'INFO',
			route: context.url.pathname,
			method: context.request.method,
			statusCode,
			latencyMs: Math.round(performance.now() - startedAt),
		};
		const log = statusCode >= 500 ? console.error : console.log;

		log(JSON.stringify(logEntry));
	}
});
