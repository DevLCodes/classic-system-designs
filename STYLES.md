# Style: the field manual

Every page in this repo uses one look: a clean, quiet reference with grey paper, crisp type, precise diagrams and 3D scenes. The voice is dense and exact, with numbers, trade-offs, failure modes and interview framing. Fonts are Bricolage Grotesque (display), Instrument Sans (body) and IBM Plex Mono (labels, code); body text is 16px at 1.6 line height in a 760px reading column.

## Tokens

Copy the `:root` block from `index.html`, never from memory:
`--bg #e9ecef`, `--paper #f7f8f9`, `--ink #1c2530`, `--muted #586473`, `--line #cdd4dc`, `--line-strong #9aa5b1`, `--accent #4255d4`, `--code-bg #eef1f4`, `--wire #7d8996`.

Diagram colours are semantic and fixed across every page (`.k-user`, `.k-serve`, `.k-kb`, and so on, each with a pale `--t-*` tint for fills). Error and dead-letter paths are `#b23a3a`, healthy paths `#2f8f5b`. Don't recolour them: a reader learns what a colour means once and relies on it everywhere.

## Layout

- The site header is identical on every page: brand "Classic System Design", then Home, Building blocks (`index.html#blocks`), Designs (`index.html#designs`), Study (`study.html`) and an external link to the agentic designs. Mark the current section with `aria-current="page"`: Home on the index, Building blocks on block pages, Designs on walkthroughs, Study on study.html.
- The home page is a card grid. Every other page is `.doc`: a sticky numbered `.toc` rail (220px) beside a 760px `article`. Sections are separated by hairlines, not decoration. Mono uppercase `.eyebrow` / `.k` labels sit above titles.
- Building block pages follow: what it is, how it works, a `#lab`, failure modes, `#interview`, `#real-world`, `#related`.
- Walkthroughs follow: requirements, estimates, API, architecture (2D figure plus 3D scene), storage, deep dives, failure and risks, observability, deployment, presenting it in an interview, related.

## Components

- `.fig` with an inline `svg.dg` diagram, or a `.fig3d` scene built with `assets/scene3d.js` and the three@0.160.0 import map. Load `assets/scene3d.css` and import `./assets/scene3d.js`.
- `.note` (accent left border), `.formula` (mono, boxed), `.table` wrappers for wide tables, `.related` pill links, `.pager` prev/next.
- `.lab` blocks for interactive calculators, in the same quiet styling.
- `.check` "Check yourself" section (`<section id="check" class="check">`), placed just before `#related` (or last, on walkthroughs that end with `#numbers`), with one TOC entry. 3 to 5 questions, each a `<details>` whose `<summary>` is the question and whose `<p class="ans">` holds a bold short answer, one or two sentences of why, and a link to the section that covers it. No JavaScript: the browser opens and closes them. The `.check` CSS (counter-numbered Q1, Q2… and a +/− marker) is copied into each page's first `<style>` block. Questions follow the deck rules: check every answer against the page, and point every link at a real section id. Pages with a deck reuse questions from its quiz.
- The footer says figures marked illustrative show the shape of a system, not measured numbers.

## Study: flashcards and quizzes

`study.html` is the hub and `study.js` is the engine (no dependencies; it injects its own `.st-*` styles from the tokens above). The hub reads the groups and order from the card grids on `index.html`, so a new page appears in the hub as soon as it has a card there and a deck.

- One deck per page at `decks/<page-slug>.json`. The format is shared with the agentic site and must not change:
  `{"title": "...", "page": "<page-slug>.html", "cards": [{"front": "term or question", "back": "1-3 plain sentences", "link": "<page-slug>.html#section-id"}], "quiz": [{"q": "...", "choices": ["four options"], "answer": 0, "why": "one sentence", "link": "<page-slug>.html#section-id"}]}`
- 8 to 12 cards and 5 to 8 questions. Four different choices, wrong ones plausible. Check every answer against the page itself, and point every link at a real section id.
- Add the slug to `decks/index.json` (a JSON list of every deck slug). The hub only fetches slugs listed there, so pages without a deck stay hidden.
- Run `python3 tools/check_decks.py` before opening a PR: it checks the format, the index list, answer indexes and that every link resolves.
- Flashcards: Space or click flips, arrow keys move, K marks a card known (saved in `localStorage`, ignored if storage is blocked), Shuffle and "Skip known cards". Quiz: 1 to 4 pick an answer, instant feedback with the why and a section link, a score at the end, and "Retry wrong ones".

## Don't

Use handwriting fonts, rotated stickies, highlighter strokes or paper textures. Those belong to the beginner notebook at DevLCodes/agentic-ai-beginner, which has its own style.

## Checklist for a new page

1. Copy the head, tokens and base CSS from an existing page of the same kind (`caching.html` for a block, `url-shortener.html` for a walkthrough).
2. Add a card for it in `index.html` under `#blocks` or `#designs`, and link it from the `#related` list of at least one neighbouring page.
3. Links to the agentic site are absolute (`https://devlcodes.github.io/agentic-ai-notebook/system-design/...`).
4. Add a `#check` section (see Components) with 3 to 5 questions.
5. Check it at 390px and 1280px wide: no horizontal scroll, 16px side gutter, 3D scene renders, lab works, no console errors.
6. Optional but welcome: a deck in `decks/<slug>.json` plus its slug in `decks/index.json`, checked with `python3 tools/check_decks.py`.
