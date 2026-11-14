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
 ("99.7", "Sandbox: four queens, reworked (app style, six phases)", "Queens 2", "ls-queens",
  "Round three: the lesson in the app's own style and in six named phases, driven by scrolling or by a timeline, with a task on the drawing.",
  "Backtracking: four queens",
  "the app's own look at the pane's width; six named phases (Problem, Brute force, Observation, Optimization, Trace, Insight), each with its text and code beside the drawing; a bar that names the phases; and a task where you act on the drawing. The three switches at the top change how the figure is driven, how the phases are shown, and how the code change is shown.",
  "Every way to put four queens on the board, as a wheel.",
  "A partial answer that already breaks the rule cannot be repaired by adding to it: drop everything that starts with it.",
  "two queens that attack each other rule out all 16 boards that begin with them."),
 ("99.8", "Sandbox: fewest coins, reworked (app style, six phases)", "Coins 2", "ls-coins",
  "Round three: the lesson in the app's own style and in six named phases. It opens on the timeline; the switch at the top changes it to scrolling.",
  "Dynamic programming: the fewest coins",
  "the same lesson kit as 99.7, opening on the timeline. Each call is written as the question it asks, dp(3), and the repeated part of the call tree is tinted once the memo makes it unnecessary.",
  "The fewest coins that make 6, as the tree of calls.",
  "The same question comes up again and again: answer it once and keep the answer.",
  "24 calls ask 7 different questions."),
 ("99.9", "Sandbox: shortest route, reworked (app style, six phases)", "Routes 2", "ls-roads",
  "Round three: the lesson in the app's own style and in six named phases, opening on scrolling, with two tasks on the map.",
  "Graphs: the shortest way between two towns",
  "the same lesson kit as 99.7, opening on scrolling. The obvious way runs slowly at first and then speeds up; in the Observation phase you press the town that is finished, twice.",
  "The shortest way from A to G.",
  "What is nearest can no longer be improved, so finish it and never look back.",
  "the nearest unfinished town cannot be reached more cheaply through a farther one, as long as every road costs something."),
 ("99.10", "Sandbox: sum of a range in a search tree (app style, six phases)", "Tree range", "ls-range",
  "Round three: a tree lesson in the app's own style and in six named phases, opening on the timeline, with a task on the tree.",
  "Trees: the sum of a range in a binary search tree",
  "the same lesson kit as 99.7 on a tree, opening on the timeline. The subtrees the fast way never enters are tinted.",
  "The sum of the values between 30 and 60 in a binary search tree.",
  "Order lets one comparison rule out a whole subtree.",
  "a node below the range rules out everything to its left, and a node above it everything to its right."),
 ("99.11", "Sandbox: a pair with a given sum (lesson kit, round four)", "Pair sum 2", "ls-pair",
  "Round four: the two-pointer lesson on the kit, with the wasteful loops boxed in the obvious code and the story held at each task.",
  "Two pointers: a pair with a given sum",
  "the lesson kit after the fourth review. The lines of the obvious code that do the wasted work are boxed in red, and the Optimization phase shows what replaces them. Scrolling and the play button stop at a task; only the phase bar goes past one. The three switches at the top change how the figure is driven, how the phases are shown, and how the code change is shown.",
  "Every pair of eight sorted numbers, and the two that add up to 21.", "", ""),
 ("99.12", "Sandbox: the minimum of every window (lesson kit, round four)", "Window 2", "ls-window",
  "Round four: the monotonic-queue lesson on the kit, opening on the timeline with the phases down a side rail.",
  "Queues: the minimum of every window",
  "the same kit as 99.11, opening on the timeline, with the phases down a side rail and the code change shown as an edit.",
  "A window of five numbers sliding along a row of twelve.", "", ""),
 ("99.13", "Sandbox: trapped rain water (lesson kit, a hard problem)", "Rain", "ls-rain",
  "Round four: a hard problem on the kit. Twelve bars, the water they hold, and one pass in place of two scans per bar.",
  "Two pointers, harder: trapped rain water",
  "the same kit as 99.11 on a problem of interview-hard level, opening on scrolling with the phases as steps.",
  "Twelve bars and the rain they hold.", "", ""),
 ("99.14", "Sandbox: the largest rectangle in a histogram (lesson kit, a hard problem)", "Histogram", "ls-hist",
  "Round four: a second hard problem on the kit. Every stretch of bars as a table, and the one rectangle per bar that the fast way measures.",
  "Stacks, harder: the largest rectangle in a histogram",
  "the same kit as 99.11 on a problem of interview-hard level, opening on the timeline with the phases as a scrubber.",
  "Six bars, and the largest rectangle that fits under them.", "", ""),
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
    open(here / sec / "text.html", "w").write(f'''<section id="story" data-source="omnistax-sandbox">
<h2>{h2}</h2>
<p>What this page tries: {tries}</p>
<figure class="sim" id="{fig}"><div class="sim-head"><span class="eyebrow">Sim</span><span>{cap}</span></div></figure>
</section>
''' + ("" if fig.startswith("ls-") else f'''<section id="recap" data-source="omnistax-sandbox">
<h2>The insight</h2>
<div class="note"><span class="eyebrow">Insight</span><p><strong>{insight}</strong> Here: {here_is}</p></div>
</section>
'''))
    open(here / sec / "source.md", "w").write(f"# Sandbox {sec}\n\nA trial page, AI-written, with no source of its own.\n")
    if sec not in have:
        ch["sections"].append({"id": sec, "title": title})
    else:
        next(s for s in ch["sections"] if s["id"] == sec)["title"] = title
json.dump(ch, open(here / "chapter.json", "w"), ensure_ascii=False, indent=2)
print([s["id"] for s in ch["sections"]])
