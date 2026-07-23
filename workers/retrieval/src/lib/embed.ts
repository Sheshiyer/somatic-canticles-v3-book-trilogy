interface EmbedResponse {
  data: Array<{ index: number; embedding: number[] }>;
  model: string;
}

const BATCH_SIZE = 16;
const MAX_TOKENS = 400;

function truncateToTokenLimit(text: string): string {
  const words = text.split(/\s+/);
  if (words.length <= MAX_TOKENS) return text;
  return words.slice(0, MAX_TOKENS).join(' ');
}

async function nimFetch(
  baseUrl: string,
  apiKey: string,
  path: string,
  body: Record<string, unknown>
): Promise<Response> {
  const url = `${baseUrl}${path}`;
  const response = await fetch(url, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      Authorization: `Bearer ${apiKey}`,
    },
    body: JSON.stringify(body),
  });

  if (!response.ok) {
    throw new Error(`NIM returned ${response.status}: ${await response.text()}`);
  }

  return response;
}

export async function embedTexts(
  texts: string[],
  env: { NIM_BASE_URL: string; NVIDIA_API_KEY: string; EMBEDDING_MODEL: string }
): Promise<number[][]> {
  if (texts.length === 0) return [];

  const batches: string[][] = [];
  for (let i = 0; i < texts.length; i += BATCH_SIZE) {
    batches.push(texts.slice(i, i + BATCH_SIZE));
  }

  const batchResults = await Promise.all(
    batches.map(async (batch) => {
      const truncated = batch.map(truncateToTokenLimit);
      const res = await nimFetch(env.NIM_BASE_URL, env.NVIDIA_API_KEY, '/embeddings', {
        input: truncated,
        model: env.EMBEDDING_MODEL,
        input_type: 'passage',
        encoding_format: 'float',
      });
      const data = (await res.json()) as EmbedResponse;
      const sorted = [...data.data].sort((a, b) => a.index - b.index);
      return sorted.map((d) => d.embedding);
    })
  );

  return batchResults.flat();
}

export async function embedQuery(
  query: string,
  env: { NIM_BASE_URL: string; NVIDIA_API_KEY: string; EMBEDDING_MODEL: string }
): Promise<number[]> {
  const res = await nimFetch(env.NIM_BASE_URL, env.NVIDIA_API_KEY, '/embeddings', {
    input: [query],
    model: env.EMBEDDING_MODEL,
    input_type: 'query',
    encoding_format: 'float',
  });
  const data = (await res.json()) as EmbedResponse;
  return data.data[0].embedding;
}
