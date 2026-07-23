import type { Chunk, ChunkMetadata } from '../types';

const CHUNK_WORDS = 200;
const OVERLAP_WORDS = 30;

function stripFrontmatter(text: string): string {
  const lines = text.split('\n');
  if (lines[0]?.trim() === '---') {
    const end = lines.indexOf('---', 1);
    if (end !== -1) {
      return lines.slice(end + 1).join('\n');
    }
  }
  return text;
}

function splitWords(text: string): string[] {
  return text.split(/\s+/).filter(Boolean);
}

export function chunkDocument(
  text: string,
  metadata: Omit<ChunkMetadata, 'chunk_index' | 'total_chunks'>
): Chunk[] {
  const cleaned = stripFrontmatter(text);
  const words = splitWords(cleaned);

  if (words.length === 0) return [];

  const chunks: Chunk[] = [];
  let start = 0;
  let index = 0;

  while (start < words.length) {
    const end = Math.min(start + CHUNK_WORDS, words.length);
    const chunkWords = words.slice(start, end);
    const chunkText = chunkWords.join(' ');

    chunks.push({
      id: `${metadata.source}:${index}`,
      text: chunkText,
      metadata: {
        ...metadata,
        chunk_index: index,
        total_chunks: 0,
      },
    });

    index++;
    start += CHUNK_WORDS - OVERLAP_WORDS;
  }

  const total = chunks.length;
  for (const chunk of chunks) {
    chunk.metadata.total_chunks = total;
  }

  return chunks;
}
