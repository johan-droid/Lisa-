# Site folder ownership guard

The `site/` folder is the curated public developer overview for Lisa.

Future agents must not overwrite this folder unless the user explicitly asks to change the public website UX, copy, or static assets.

## Do not put these in `site/`

- Generated reports
- Test output
- Final closure notes
- Deployment checklists
- Backend architecture dumps
- Temporary agent output
- Markdown converted into a placeholder HTML page
- Runtime logs or artifacts

## Correct locations

- Use `docs/` for architecture, deployment guides, smoke-test instructions, and final reports.
- Use `backend/` for runtime code, services, persistence, workers, brains, queues, and integrations.
- Use `tests/` for regression tests.
- Use `scripts/` for local drills and developer utilities.

## Allowed edits to `site/`

Only edit `site/index.html`, `site/styles.css`, or `site/script.js` when the task explicitly says to update the public website.

The site must remain a polished developer-facing landing page that explains Lisa's architecture, data flow, brain map, runtime safety, deployment readiness, and site ownership guard.
