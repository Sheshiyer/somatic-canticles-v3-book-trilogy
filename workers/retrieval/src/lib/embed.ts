import type { EmbeddingResponse } from '../types';

export async function embedTexts(
  texts: string[],
  env: { EMBEDDING_WORKER_URL: string; EMBEDDING_MODEL: string }
): Promise<number[][]> {
  const url = `${env.EMBEDDING_WORKER_URL}/test/eval-embed`;

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      texts,
      model: env.EMBEDDING_MODEL,
      input_type: 'passage',
    }),
  });

  if (!response.ok) {
    throw new Error(`Embedding Worker returned ${response.status}: ${await response.text()}`);
  }

  const data = (await response.json()) as EmbeddingResponse;
  return data.vectors;
}

export async function embedQuery(
  query: string,
  env: { EMBEDDING_WORKER_URL: string; EMBEDDING_MODEL: string }
): Promise<number[]> {
  const url = `${env.EMBEDDING_WORKER_URL}/test/eval-embed`;

  const response = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      texts: [query],
      model: env.EMBEDDING_MODEL,
      input_type: 'query',
    }),
  });

  if (!response.ok) {
    throw new Error(`Embedding Worker returned ${response.status}: ${await response.text()}`);
  }

  const data = (await response.json()) as EmbeddingResponse;
  return data.vectors[0];
}
