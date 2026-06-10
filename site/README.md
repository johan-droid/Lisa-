# Lisa public site ownership guard

This folder is the public Lisa landing page.

## Hard rule

Do **not** replace `site/index.html`, `site/styles.css`, or `site/script.js` with:

- a generated status report,
- a plain implementation checklist,
- a temporary debugging page,
- a markdown-to-HTML dump,
- an agent closure report,
- or backend architecture documentation.

Those materials belong in `docs/`, `reports/`, or root-level project documentation — not in `site/`.

## What belongs here

Only public-facing static landing page assets belong here:

- polished product/brand HTML,
- responsive CSS,
- small static JavaScript for navigation, tabs, or page-only interaction,
- images or public static assets used by the page.

## Before editing

An agent may edit this folder only when the explicit task is to change the public website UX/content/assets. Otherwise, leave `site/` untouched.

If a task needs to document implementation status, update `docs/` instead.
