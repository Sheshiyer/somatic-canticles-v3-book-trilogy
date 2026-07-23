import type { Env, Chunk, IngestResponse } from '../types';
import { chunkDocument } from './chunk';
import { embedTexts } from './embed';

const BATCH_SIZE = 32;

interface CorpusFile {
  source: string;
  book: number;
  chapter: number;
  title: string;
  content: string;
}

export async function ingestCorpus(
  files: CorpusFile[],
  env: Env
): Promise<IngestResponse> {
  const allChunks: Chunk[] = [];
  const errors: string[] = [];

  for (const file of files) {
    try {
      const chunks = chunkDocument(file.content, {
        source: file.source,
        book: file.book,
        chapter: file.chapter,
        title: file.title,
      });
      allChunks.push(...chunks);
    } catch (err) {
      errors.push(`${file.source}: ${err instanceof Error ? err.message : String(err)}`);
    }
  }

  let ingested = 0;

  for (let i = 0; i < allChunks.length; i += BATCH_SIZE) {
    const batch = allChunks.slice(i, i + BATCH_SIZE);
    const texts = batch.map((c) => c.text);

    try {
      const vectors = await embedTexts(texts, env);

      const upserts = batch.map((chunk, j) => ({
        id: chunk.id,
        values: vectors[j],
        metadata: {
          text: chunk.text,
          source: chunk.metadata.source,
          book: chunk.metadata.book,
          chapter: chunk.metadata.chapter,
          title: chunk.metadata.title,
          chunk_index: chunk.metadata.chunk_index,
          total_chunks: chunk.metadata.total_chunks,
        },
      }));

      await env.CORPUS_INDEX.upsert(upserts);
      ingested += batch.length;
    } catch (err) {
      errors.push(
        `batch ${i}-${i + BATCH_SIZE}: ${err instanceof Error ? err.message : String(err)}`
      );
    }
  }

  return {
    ingested,
    chunks: allChunks.length,
    errors,
  };
}
