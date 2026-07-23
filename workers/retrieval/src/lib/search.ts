import type { Env, SearchResult, SearchResponse } from '../types';
import { embedQuery } from './embed';

export async function searchCorpus(
  query: string,
  topK: number,
  env: Env
): Promise<SearchResponse> {
  const vector = await embedQuery(query, env);

  const matches = await env.CORPUS_INDEX.query(vector, {
    topK,
    returnMetadata: 'all',
  });

  const results: SearchResult[] = matches.matches.map((match) => ({
    id: match.id,
    score: match.score,
    text: (match.metadata as Record<string, string>)?.text ?? '',
    metadata: {
      source: (match.metadata as Record<string, string>)?.source ?? '',
      book: Number((match.metadata as Record<string, string>)?.book) || 0,
      chapter: Number((match.metadata as Record<string, string>)?.chapter) || 0,
      title: (match.metadata as Record<string, string>)?.title ?? '',
      chunk_index: Number((match.metadata as Record<string, string>)?.chunk_index) || 0,
      total_chunks: Number((match.metadata as Record<string, string>)?.total_chunks) || 0,
    },
  }));

  return {
    query,
    results,
    count: results.length,
    model: env.EMBEDDING_MODEL,
  };
}
