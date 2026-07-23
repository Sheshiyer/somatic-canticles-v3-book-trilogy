import { Hono } from 'hono';
import { cors } from 'hono/cors';
import { logger } from 'hono/logger';
import { poweredBy } from 'hono/powered-by';
import type { Env } from './types';

import ingestRoutes from './routes/ingest';
import searchRoutes from './routes/search';

const app = new Hono<{ Bindings: Env }>();

app.use('*', cors());
app.use('*', logger());
app.use('*', poweredBy());

app.get('/health', (c) => {
  return c.json({
    status: 'ok',
    timestamp: new Date().toISOString(),
    environment: c.env.ENVIRONMENT,
  });
});

app.get('/', (c) => {
  return c.json({
    name: 'Somatic Canticles Retrieval API',
    version: '1.0.0',
    endpoints: {
      health: '/health',
      search: 'POST /api/v1/search',
      ingest: 'POST /api/v1/ingest',
    },
  });
});

app.route('/api/v1/ingest', ingestRoutes);
app.route('/api/v1/search', searchRoutes);

app.notFound((c) => {
  return c.json(
    { success: false, error: 'Not Found' },
    404
  );
});

app.onError((err, c) => {
  console.error('Error:', err);
  return c.json(
    {
      success: false,
      error: c.env.ENVIRONMENT === 'development' ? err.message : 'Internal Server Error',
    },
    500
  );
});

export default app;
