import { Hono } from 'hono';
import type { Env, ApiResponse, IngestResponse } from '../types';
import { ingestCorpus } from '../lib/ingest';

const ingestRoutes = new Hono<{ Bindings: Env }>();

ingestRoutes.post('/', async (c) => {
  try {
    const body = await c.req.json();

    if (!body.files || !Array.isArray(body.files)) {
      return c.json(
        { success: false, error: 'files must be a non-empty array' } satisfies ApiResponse<never>,
        400
      );
    }

    const result = await ingestCorpus(body.files, c.env);

    return c.json({
      success: true,
      data: result,
    } satisfies ApiResponse<IngestResponse>);
  } catch (err) {
    return c.json(
      {
        success: false,
        error: err instanceof Error ? err.message : 'Ingestion failed',
      } satisfies ApiResponse<never>,
      500
    );
  }
});

export default ingestRoutes;
