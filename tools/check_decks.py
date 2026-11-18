#!/usr/bin/env python3
"""Validate every decks/<slug>.json against the shared deck format (see STYLES.md, Study).

Run from anywhere:  python3 tools/check_decks.py
Exit code 0 means every deck is valid; otherwise each problem is printed as `path: message`.
"""
from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DECKS = ROOT / "decks"
DECK_KEYS = {"title", "page", "cards", "quiz"}
CARD_KEYS = {"front", "back", "link"}
QUIZ_KEYS = {"q", "choices", "answer", "why", "link"}

problems: list[str] = []
_ids: dict[Path, set[str]] = {}


def fail(path: Path, msg: str) -> None:
    problems.append(f"{path.relative_to(ROOT)}: {msg}")


class _IdParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        for k, v in attrs:
            if k == "id" and v:
                self.ids.add(v)


def ids_of(page: Path) -> set[str]:
    if page not in _ids:
        p = _IdParser()
        p.feed(page.read_text(encoding="utf-8"))
        _ids[page] = p.ids
    return _ids[page]


def nonempty(v) -> bool:
    return isinstance(v, str) and bool(v.strip())


def check() -> None:
    files = sorted(p.stem for p in DECKS.glob("*.json") if p.name != "index.json")
    manifest = DECKS / "index.json"
    try:
        listed = json.loads(manifest.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        listed = None
    if not isinstance(listed, list) or sorted(listed) != files or len(set(listed)) != len(listed):
        fail(manifest, f"must be a JSON list of every deck slug in decks/, exactly: {json.dumps(files)}")

    for path in sorted(p for p in DECKS.glob("*.json") if p.name != "index.json"):
        try:
            deck = json.loads(path.read_text(encoding="utf-8"))
        except ValueError as e:
            fail(path, f"not valid JSON: {e}")
            continue
        if not isinstance(deck, dict) or set(deck) != DECK_KEYS:
            fail(path, f"deck keys must be exactly {sorted(DECK_KEYS)}")
            continue
        slug = path.stem
        if deck["page"] != f"{slug}.html":
            fail(path, f'"page" should be "{slug}.html"')
        if not (ROOT / f"{slug}.html").exists():
            fail(path, f"no page {slug}.html")
        if not nonempty(deck["title"]):
            fail(path, '"title" must be a non-empty string')
        cards, quiz = deck["cards"], deck["quiz"]
        if not isinstance(cards, list) or not 8 <= len(cards) <= 12:
            fail(path, "needs 8 to 12 cards")
            cards = cards if isinstance(cards, list) else []
        if not isinstance(quiz, list) or not 5 <= len(quiz) <= 8:
            fail(path, "needs 5 to 8 quiz questions")
            quiz = quiz if isinstance(quiz, list) else []

        links: list[tuple[str, str]] = []
        fronts: list[str] = []
        for n, c in enumerate(cards, 1):
            if not isinstance(c, dict) or set(c) != CARD_KEYS or not all(nonempty(c[k]) for k in c):
                fail(path, f"card {n} needs non-empty front, back and link only")
                continue
            fronts.append(c["front"])
            links.append((f"card {n}", c["link"]))
        for dup in sorted({f for f in fronts if fronts.count(f) > 1}):
            fail(path, f"card front used twice: {dup}")

        for n, q in enumerate(quiz, 1):
            if not isinstance(q, dict) or set(q) != QUIZ_KEYS:
                fail(path, f"question {n} needs exactly q, choices, answer, why and link")
                continue
            ch = q["choices"]
            if not isinstance(ch, list) or len(ch) != 4 or not all(nonempty(x) for x in ch) or len(set(ch)) != 4:
                fail(path, f"question {n} needs 4 different non-empty choices")
            elif not isinstance(q["answer"], int) or isinstance(q["answer"], bool) or not 0 <= q["answer"] < 4:
                fail(path, f"question {n} answer index {q['answer']!r} is out of range")
            if not all(nonempty(q[k]) for k in ("q", "why", "link")):
                fail(path, f"question {n} needs non-empty q, why and link")
                continue
            links.append((f"question {n}", q["link"]))

        for where, link in links:
            page, _, frag = link.partition("#")
            target = ROOT / page
            if not page.endswith(".html") or "/" in page or not target.exists():
                fail(path, f"{where} link {link} is not a page in this repo")
            elif not frag:
                fail(path, f"{where} link {link} needs a #section id")
            elif frag not in ids_of(target):
                fail(path, f"{where} link {link} points at a missing #{frag}")


if __name__ == "__main__":
    check()
    for p in problems:
        print(p)
    n = len([p for p in DECKS.glob("*.json") if p.name != "index.json"])
    print(f"{n} decks checked, {len(problems)} problem(s)", file=sys.stderr)
    sys.exit(1 if problems else 0)
