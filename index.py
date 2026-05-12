"""
Vercel serverless entry for FastAPI. Route `/api/*` rewrites here (see vercel.json).
Requires env `DATABASE_URL` (Vercel Postgres, Neon, Supabase, etc.).
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from database import init_db

init_db()

from backend import app  # noqa: E402
