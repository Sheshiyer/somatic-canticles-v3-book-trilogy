import { Hono } from 'hono';
import type { Env, ApiResponse, SearchResponse } from '../types';
import { searchCorpus } from '../lib/search';

const searchRoutes = new Hono<{ Bindings: Env }>();

searchRoutes.post('/', async (c) => {
  try {
    const body = await c.req.json();

    if (!body.query || typeof body.query !== 'string') {
      return c.json(
        { success: false, error: 'query must be a non-empty string' } satisfies ApiResponse<never>,
        400
      );
    }

    const topK = typeof body.topK === 'number' && body.topK > 0 ? body.topK : 10;

    const result = await searchCorpus(body.query, topK, c.env);

    return c.json({
      success: true,
      data: result,
    } satisfies ApiResponse<SearchResponse>);
  } catch (err) {
    return c.json(
      {
        success: false,
        error: err instanceof Error ? err.message : 'Search failed',
      } satisfies ApiResponse<never>,
      500
    );
  }
});

export default searchRoutes;
