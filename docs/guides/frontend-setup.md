# Frontend setup

This project uses a Vite + React SPA for the investor and analyst research experience, authenticated workflows, and a clean connection to the FastAPI backend. Server rendering and SEO are not required for this application.

## Init (from empty `frontend/`)

```bash
cd frontend
pnpm create vite . --template react-ts
pnpm install
pnpm add react-router-dom @supabase/supabase-js
pnpm add -D tailwindcss @tailwindcss/vite
pnpm dlx shadcn@latest init
```

## Run

```bash
cd frontend
pnpm install
pnpm dev
```

## Check

```bash
pnpm tsc --noEmit
pnpm lint
```
