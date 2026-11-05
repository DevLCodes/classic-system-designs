# Style: the field manual

Every page in this repo uses one look: a clean, quiet reference with grey paper, crisp type, precise diagrams and 3D scenes. The voice is dense and exact, with numbers, trade-offs, failure modes and interview framing. Fonts are Bricolage Grotesque (display), Instrument Sans (body) and IBM Plex Mono (labels, code); body text is 16px at 1.6 line height in a 760px reading column.

## Tokens

Copy the `:root` block from `index.html`, never from memory:
`--bg #e9ecef`, `--paper #f7f8f9`, `--ink #1c2530`, `--muted #586473`, `--line #cdd4dc`, `--line-strong #9aa5b1`, `--accent #4255d4`, `--code-bg #eef1f4`, `--wire #7d8996`.

Diagram colours are semantic and fixed across every page (`.k-user`, `.k-serve`, `.k-kb`, and so on, each with a pale `--t-*` tint for fills). Error and dead-letter paths are `#b23a3a`, healthy paths `#2f8f5b`. Don't recolour them: a reader learns what a colour means once and relies on it everywhere.

## Layout

- The site header is identical on every page: brand "Classic System Design", then Home, Building blocks (`index.html#blocks`), Designs (`index.html#designs`) and an external link to the agentic designs. Mark the current section with `aria-current="page"`: Home on the index, Building blocks on block pages, Designs on walkthroughs.
- The home page is a card grid. Every other page is `.doc`: a sticky numbered `.toc` rail (220px) beside a 760px `article`. Sections are separated by hairlines, not decoration. Mono uppercase `.eyebrow` / `.k` labels sit above titles.
- Building block pages follow: what it is, how it works, a `#lab`, failure modes, `#interview`, `#real-world`, `#related`.
- Walkthroughs follow: requirements, estimates, API, architecture (2D figure plus 3D scene), storage, deep dives, failure and risks, observability, deployment, presenting it in an interview, related.

## Components

- `.fig` with an inline `svg.dg` diagram, or a `.fig3d` scene built with `assets/scene3d.js` and the three@0.160.0 import map. Load `assets/scene3d.css` and import `./assets/scene3d.js`.
- `.note` (accent left border), `.formula` (mono, boxed), `.table` wrappers for wide tables, `.related` pill links, `.pager` prev/next.
- `.lab` blocks for interactive calculators, in the same quiet styling.
- The footer says figures marked illustrative show the shape of a system, not measured numbers.

## Don't

Use handwriting fonts, rotated stickies, highlighter strokes or paper textures. Those belong to the beginner notebook at DevLCodes/agentic-ai-beginner, which has its own style.

## Checklist for a new page

1. Copy the head, tokens and base CSS from an existing page of the same kind (`caching.html` for a block, `url-shortener.html` for a walkthrough).
2. Add a card for it in `index.html` under `#blocks` or `#designs`, and link it from the `#related` list of at least one neighbouring page.
3. Links to the agentic site are absolute (`https://devlcodes.github.io/agentic-ai-notebook/system-design/...`).
4. Check it at 390px and 1280px wide: no horizontal scroll, 16px side gutter, 3D scene renders, lab works, no console errors.
