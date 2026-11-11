"""Writes the section.json, text.html and source.md of each one-figure sandbox page, and lists them in chapter.json.

    python3 ch99/_kit/pages.py
"""
import json, os, pathlib
here = pathlib.Path(__file__).parent.parent
PAGES = [
 ("99.3", "Sandbox: fewest coins (one morphing timeline, blackboard)", "Coins", "xp-coins",
  "The whole lesson is one drawing on one clock: the call tree of the obvious recursion folds up into the table.",
  "Dynamic programming: the fewest coins",
  "the story told by one drawing that changes shape, and a look that ignores the figure rules (its own dark palette, one colour per question, large type, no code panel). Press play, or drag along the bar. In the first two chapters, point at a circle to see every other call that asks the same question.",
  "The fewest coins that make 7, from the call tree to the table.",
  "The same question comes up again and again: answer it once and keep the answer.",
  "39 calls ask 8 different questions, and each question needs only smaller ones."),
 ("99.4", "Sandbox: shortest route (a race on one clock, transit map)", "Routes", "xp-roads",
  "The whole lesson is one clock driving two panels: the obvious way and the fast way race on the same map, then the fast way is replayed with the reader choosing.",
  "Graphs: the shortest way between two towns",
  "a split screen on one clock, the clock waiting for the reader at three points, and a look that ignores the figure rules (a paper map whatever the theme, thick lines, colour by what a distance is worth, no code at all). Press play. In the second chapter the story stops three times until you click a town.",
  "The shortest way from A to G, raced two ways.",
  "What is nearest can no longer be improved, so finish it and never look back.",
  "the nearest unfinished town cannot be reached more cheaply through a farther one, as long as every road costs something."),
 ("99.5", "Sandbox: four queens (scrolling drives the story, print look)", "Queens", "xp-queens",
  "The whole lesson is one drawing that stays put while the text scrolls past it; where you are in the text is where the drawing is in the story.",
  "Backtracking: four queens",
  "the reader's own scrolling as the clock, and a look that ignores the figure rules (a printed page whatever the theme, one accent colour, serif numerals, a wheel in place of a tree). Scroll slowly through the steps on the right. Point at the wheel to see the board any wedge stands for.",
  "Every way to put four queens on the board, as a wheel.",
  "A partial answer that already breaks the rule cannot be repaired by adding to it: drop everything that starts with it.",
  "two queens that attack each other rule out all 16 boards that begin with them."),
 ("99.6", "Sandbox: the number without a twin (the reader's answers move the story, LED panel)", "Twins", "xp-twin",
  "The whole lesson is one panel that moves on only when the reader acts: there is no play button.",
  "Bit manipulation: the number without a twin",
  "a story with no clock, where each step ends with something for the reader to do, and a look that ignores the figure rules (a dark panel of lamps whatever the theme, a monospaced face throughout, the code set as large as the drawing).",
  "Seven numbers, six of them in pairs, as lamps.",
  "Something that undoes itself when applied twice makes pairs vanish, in any order.",
  "x XOR x is 0, so XOR-ing everything together leaves only the number that has no twin."),
]
ch = json.load(open(here / "chapter.json"))
have = {s["id"] for s in ch["sections"]}
for sec, title, short, fig, lead, h2, tries, cap, insight, here_is in PAGES:
    if not (here / "_kit" / (sec + ".js")).exists():
        continue
    os.makedirs(here / sec, exist_ok=True)
    json.dump({"id": sec, "chapter": "99", "title": title, "short": short,
               "lead": "A sandbox page, AI-written and not part of the book. " + lead,
               "objectives": [], "summary_html": "", "notes": "A trial page: nothing here is the book's.", "built": "2026-11-11",
               "figures": [{"id": fig, "kind": "sim", "draws": []}], "coverage": [], "exercises": [], "exercise_concepts": [],
               "referents": [], "footnotes": [], "derivations": []}, open(here / sec / "section.json", "w"), ensure_ascii=False, indent=1)
    open(here / sec / "text.html", "w").write(f'''<section id="story">
<h2>{h2}</h2>
<p>What this page tries: {tries}</p>
<figure class="sim" id="{fig}"><div class="sim-head"><span class="eyebrow">Sim</span><span>{cap}</span></div></figure>
</section>
<section id="recap">
<h2>The insight</h2>
<div class="note"><span class="eyebrow">Insight</span><p><strong>{insight}</strong> Here: {here_is}</p></div>
</section>
''')
    open(here / sec / "source.md", "w").write(f"# Sandbox {sec}\n\nA trial page, AI-written, with no source of its own.\n")
    if sec not in have:
        ch["sections"].append({"id": sec, "title": title})
    else:
        next(s for s in ch["sections"] if s["id"] == sec)["title"] = title
json.dump(ch, open(here / "chapter.json", "w"), ensure_ascii=False, indent=2)
print([s["id"] for s in ch["sections"]])
