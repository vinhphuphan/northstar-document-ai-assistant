# TODOs

## 1. Align the project contract
- [ ] Keep the MVP scope fixed to FPT, VCB, MWG, and VIC for 2021–2025, using the available BCTN and consolidated annual BCTC reports.
- [ ] Finalize Gemini generation and embedding model choices; verify embedding output dimensions against the planned pgvector column.
- [ ] Define supported financial metrics, units, fiscal-year rules, missing-data behavior, and how every calculated result cites its source inputs.
- [ ] Define PDF page-number semantics, extraction acceptance criteria, and when OCR is required.
- [ ] Keep README, brief, architecture, setup guides, env examples, and agent instructions consistent with the locked stack and MVP scope.

## 2. Build the service foundations
- [ ] Initialize the FastAPI app and backend package configuration so `uv sync` and documented `uv run` commands work from `backend/`.
- [ ] Add `app/config.py` as the single backend environment source; validate required settings at startup without `os.getenv` or `load_dotenv` in app modules.
- [ ] Add a health endpoint, CORS, structured logging, and a small baseline of backend unit tests.
- [ ] Scaffold the Vite + React + TypeScript SPA with pnpm, Tailwind, shadcn/ui, React Router, and the `@/*` alias.
- [ ] Add `src/lib/env.ts` and verify frontend environment values at startup; do not read `import.meta.env` elsewhere.
- [ ] Confirm secret, local corpus, and generated-file ignore rules; keep service-role credentials and database URLs out of frontend config.

## 3. Set up Supabase and schema
- [ ] Create a development Supabase project and configure email authentication.
- [ ] Add SQLAlchemy models and Alembic configuration for source documents, chunks, financial data, chats, messages, and citations.
- [ ] Create reviewed migrations for pgvector, full-text search, indexes, and RLS policies; use the direct/session database connection.
- [ ] Verify ownership checks for chat threads and messages and access rules for stored documents.

## 4. Ingest and verify the demo corpus
- [ ] Validate `data/manifest.json` against local PDFs and report missing, unreadable, or incorrectly classified files.
- [ ] Evaluate PDF extraction on representative Vietnamese annual reports and financial statements, including tables and page boundaries.
- [ ] Implement repeatable ingestion that preserves ticker, company, report type, reporting year, page, section, source URL, and extraction metadata.
- [ ] Implement page-aware chunking and Gemini embeddings; ensure the embedding model, output dimensions, and schema agree.
- [ ] Make ingestion safe to rerun and report counts/errors per document.
- [ ] Add backend unit tests for manifest validation, extraction, page mapping, chunking, and ingestion failures.
- [ ] Define a validation workflow for structured financial figures before persisting them as trusted `financial_data`.

## 5. Implement retrieval and analysis
- [ ] Add bounded semantic and PostgreSQL full-text queries with ticker, report type, and year filters.
- [ ] Fuse ranked results with Reciprocal Rank Fusion and retrieve passages with citation metadata and useful surrounding context.
- [ ] Implement deterministic metric calculations such as YoY growth, CAGR, and margins; retain references to every input value.
- [ ] Add unit tests for retrieval filters, ranking, units, missing years, invalid values, and calculations.

## 6. Implement grounded chat
- [ ] Verify Supabase bearer tokens at the FastAPI boundary and reject unauthorized requests before retrieval or model calls.
- [ ] Add chat thread/history APIs with user ownership checks and persistence.
- [ ] Define typed chat, answer, citation, source-passage, and calculation contracts.
- [ ] Implement the chat orchestration flow: retrieve evidence, calculate when required, generate with Gemini, validate grounding, then persist.
- [ ] Reject citations outside the current request's retrieved evidence; return an explicit insufficient-evidence response when needed.
- [ ] Add streaming with documented event/error behavior and persist only completed, validated assistant responses.
- [ ] Test auth, ownership, retrieval, calculation, citations, grounding failures, and persistence without live services; mark live integrations separately.

## 7. Complete the user workflow
- [ ] Implement the shared `fetch` API client with automatic bearer-token injection, timeouts, and typed API errors.
- [ ] Add email sign-in, authenticated chat history, thread creation, and message streaming.
- [ ] Render answers, report/page citations, supporting passages, calculated metrics, and reported-versus-calculated distinctions.
- [ ] Add loading, empty, network-error, and insufficient-evidence states.
- [ ] Manually verify frontend workflows in a browser; run `pnpm tsc --noEmit` and `pnpm lint` (no frontend test runner per repo instructions).

## 8. Verify and deploy
- [ ] Run backend unit tests and lint; ensure the fast test suite requires no network or database.
- [ ] Verify representative brief questions across the four tickers and five years, including page-level citations and calculations.
- [ ] Confirm unsupported claims are refused and the assistant does not produce investment recommendations.
- [ ] Configure Railway frontend/backend services and production environment variables.
- [ ] Apply reviewed Alembic migrations to the intended Supabase project and verify RLS behavior.
- [ ] Document local setup, corpus ingestion, migrations, testing, and deployment.
