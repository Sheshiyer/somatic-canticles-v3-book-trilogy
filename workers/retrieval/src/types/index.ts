export interface Env {
  CORPUS_INDEX: VectorizeIndex;
  ENVIRONMENT: string;
  NIM_BASE_URL: string;
  NVIDIA_API_KEY: string;
  EMBEDDING_MODEL: string;
  EMBEDDING_DIMS: string;
  [key: string]: unknown;
}

export interface Chunk {
  id: string;
  text: string;
  metadata: ChunkMetadata;
}

export interface ChunkMetadata {
  source: string;
  book: number;
  chapter: number;
  title: string;
  chunk_index: number;
  total_chunks: number;
}

export interface EmbeddingResponse {
  vectors: number[][];
  dimensions: number;
  model: string;
}

export interface SearchResult {
  id: string;
  score: number;
  text: string;
  metadata: ChunkMetadata;
}

export interface SearchResponse {
  query: string;
  results: SearchResult[];
  count: number;
  model: string;
}

export interface IngestResponse {
  ingested: number;
  chunks: number;
  errors: string[];
}

export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  error?: string;
}
