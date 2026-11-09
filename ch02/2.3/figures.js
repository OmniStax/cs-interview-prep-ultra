/* Figures for section 2.3 Two pointers and sliding windows. Boots against the section's text article.
   Four debugger figures (code beside the drawing, stepped by block: METHOD §2.3) and one moving figure with no
   code (a formula, config item 14). The code in sim-two-pointers, sim-three-sum and sim-merge is TheAlgorithms/
   Python's (MIT) as the source prints it, its docstring of doctests left out; their Java, C++ and JavaScript are
   AI translations (METHOD decision 20). sim-variable-window's code is doocs/leetcode 0713's in all four
   languages, as the source prints them. Each trace is the figure's own JS copy of the Python, numbered with the
   Python's lines. Indices are drawn from 0, as the code counts. */
window.OMNISTAX_FIGURES = window.OMNISTAX_FIGURES || {};
window.OMNISTAX_FIGURES['2.3'] = function (root, F) {
const { C, PAL, alpha, text, line, arrow, begin, tex, ctl, register, cycle, topline } = F;
const sim = (id, H) => F.sim(root, id, H);
const AI = 'claude-opus-5-5 high';
const AIS3 = { java: AI, cpp: AI, javascript: AI };
const J = (a) => a.join('\n');
/* a canonical line → its line in another language: the same, except where listed */
const lines = (n, extra) => { const m = {}; for (let i = 1; i <= n; i += 1) m[i] = i; return Object.assign(m, extra || {}); };
const rect = (ctx, x, y, w, h, fill, stroke, lw = 2, dash) => {
  ctx.save();
  if (fill) { ctx.fillStyle = fill; ctx.fillRect(x, y, w, h); }
  if (stroke) { ctx.strokeStyle = stroke; ctx.lineWidth = lw; if (dash) ctx.setLineDash(dash); ctx.strokeRect(x, y, w, h); }
  ctx.restore();
};
const neg = (v) => String(v).replace('-', '−');
/* A row of array cells: the values in key's colour, the indices under them in index's (26 units, the canvas
   text floor of this book's debugger figures). Returns the layout F.ds.pointer and F.ds.region draw on. */
function cells(ctx, o) {
  const n = o.values.length, cell = o.cell ?? Math.min(120, (o.w ?? 1100) / Math.max(1, n)), h = o.h ?? 72;
  const l = o.x0 ?? (o.cx ?? 700) - (n * cell) / 2, t = o.y - h / 2;
  const S = { l, r: l + n * cell, t, b: t + h, cell, n, base: 0, y: o.y, x: (i) => l + (i + 0.5) * cell };
  const key = C('key'), idx = C('index');
  o.values.forEach((v, i) => {
    const st = o.state ? o.state(i) : 'live';      /* live | faded | hollow | hot */
    const x0 = l + i * cell;
    rect(ctx, x0, t, cell, h, PAL.panel, st === 'faded' ? alpha(PAL.ink, 0.25) : st === 'hollow' ? alpha(PAL.ink, 0.45) : PAL.ink, st === 'hot' ? 4 : 2, st === 'hollow' ? [6, 6] : undefined);
    text(ctx, neg(v), x0 + cell / 2, o.y, st === 'faded' ? alpha(key, 0.35) : key, { size: o.size ?? 32, align: 'center', weight: st === 'hot' ? 600 : 400 });
    if (o.index !== false) text(ctx, String(i), x0 + cell / 2, S.b + 24, st === 'faded' ? alpha(idx, 0.45) : idx, { size: 26, align: 'center' });
  });
  if (o.name) text(ctx, o.name, l - 22, o.y, o.nameColor ?? PAL.ink, { size: 34, weight: 600, align: 'right', italic: true });
  return S;
}
const ptr = (ctx, S, list, side) => F.ds.pointer(ctx, S, list, { side: side || 'above', size: 30 });

/* ================================================================ sim-two-pointers: TheAlgorithms two_pointer */
(function () {
  const PY = J([
    'def two_pointer(nums: list[int], target: int) -> list[int]:',
    '    i = 0',
    '    j = len(nums) - 1',
    '',
    '    while i < j:',
    '        if nums[i] + nums[j] == target:',
    '            return [i, j]',
    '        elif nums[i] + nums[j] < target:',
    '            i = i + 1',
    '        else:',
    '            j = j - 1',
    '',
    '    return []',
  ]);
  const braces = (head, len, ret, empty, eq) => J([
    head,
    '    int i = 0;',
    `    int j = ${len} - 1;`,
    '',
    '    while (i < j) {',
    `        if (nums[i] + nums[j] ${eq} target) {`,
    `            return ${ret};`,
    '        } else if (nums[i] + nums[j] < target) {',
    '            i = i + 1;',
    '        } else {',
    '            j = j - 1;',
    '        }',
    '    }',
    '',
    `    return ${empty};`,
    '}',
  ]);
  const JAVA = braces('static int[] twoPointer(int[] nums, int target) {', 'nums.length', 'new int[] {i, j}', 'new int[] {}', '==');
  const CPP = braces('std::vector<int> twoPointer(const std::vector<int>& nums, int target) {', '(int) nums.size()', '{i, j}', '{}', '==');
  const JS = braces('function twoPointer(nums, target) {', 'nums.length', '[i, j]', '[]', '===').replace('    int i = 0;', '    let i = 0;').replace('    int j = ', '    let j = ');
  const MAP = lines(13, { 13: 15 });
  const run = (A, t) => F.trace((at) => {
    let i = 0, checks = 0; at(2, { i, checks });
    let j = A.length - 1; at(3, { i, j, checks });
    while (i < j) {
      at(5, { i, j, checks });
      const s = A[i] + A[j]; checks += 1;
      at(6, { i, j, 'nums[i] + nums[j]': s, target: t, checks });
      if (s === t) { at(7, { i, j, 'nums[i] + nums[j]': s, target: t, checks }, ['found', i, j]); return; }
      at(8, { i, j, 'nums[i] + nums[j]': s, target: t, checks });
      if (s < t) { i = i + 1; at(9, { i, j, 'nums[i] + nums[j]': s, target: t, checks }, ['up', i - 1]); }
      else { at(10, { i, j, 'nums[i] + nums[j]': s, target: t, checks }); j = j - 1; at(11, { i, j, 'nums[i] + nums[j]': s, target: t, checks }, ['down', j + 1]); }
    }
    at(13, { i, j, target: t, checks }, ['none']);
  });
  const INPUTS = [
    { value: 'hit', label: 'hit', A: [2, 4, 5, 7, 9, 12, 14, 18], t: 21 },
    { value: 'miss', label: 'miss', A: [2, 4, 5, 7, 9, 12, 14, 18], t: 15 },
    { value: 'dup', label: 'duplicates', A: [1, 3, 3], t: 6 },
    { value: 'adv', label: 'adversarial', A: [5, 8, 12, 16, 18, 19, 20, 21], t: 34 },
  ];
  const d = sim('sim-two-pointers', 800);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS3,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'init', lines: [2, 3], label: 'start at both ends', touches: ['i', 'j'] },
      { id: 'loop', lines: [5, 11], label: 'one check, one move' },
      { id: 'check', lines: [6, 7], label: 'compare nums[i] + nums[j] with the target', touches: ['nums[i] + nums[j]'] },
      { id: 'move', lines: [8, 11], label: 'too small: i moves right; too big: j moves left', touches: ['i', 'j'] },
    ],
    refs: { i: () => F.ref('pair-l'), j: () => F.ref('pair-r') },
  });
  F.debug(d, {
    code, watch: ['i', 'j', 'nums[i] + nums[j]', 'target', 'checks'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, x.t) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length, t = inp.t;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const I = typeof v.i === 'number' ? v.i : 0, Jn = typeof v.j === 'number' ? v.j : n - 1;
      const cl = F.ref('pair-l'), cr = F.ref('pair-r'), idx = C('index'), key = C('key');
      const found = ev[0] === 'found';
      /* the headline: the check and the move it forces, in the numbers of this run */
      let head;
      if (L <= 3) head = `i = 0 and j = ${n - 1}: any pair could still sum to the target ${t}.`;
      else if (L === 5) head = `i = ${I} < j = ${Jn}: the pairs still possible lie between them.`;
      else if (L === 6 || L === 8 || L === 10) { const s = A[I] + A[Jn]; head = `nums[${I}] + nums[${Jn}] = ${A[I]} + ${A[Jn]} = ${s} ${s === t ? '=' : s < t ? '<' : '>'} ${t}`; }
      else if (L === 7) head = `${A[I]} + ${A[Jn]} = ${t}: the pair is at i = ${I}, j = ${Jn}.`;
      else if (L === 9) head = `${A[I - 1]} + ${A[Jn]} < ${t}: no pair with nums[${I - 1}] = ${A[I - 1]} reaches ${t}, so i moves right.`;
      else if (L === 11) head = `${A[I]} + ${A[Jn + 1]} > ${t}: every pair with nums[${Jn + 1}] = ${A[Jn + 1]} is too big, so j moves left.`;
      else head = `i = j = ${I}: no pair sums to ${t}.`;
      topline(ctx, head);
      /* the array: cells outside [i, j] are ruled out (faded), the window between them tinted */
      const S = cells(ctx, { values: A, y: 220, state: (k) => (k < I || k > Jn ? 'faded' : found && (k === I || k === Jn) ? 'hot' : 'live') });
      const ei = g.num('i'), ej = g.num('j');
      F.ds.region(ctx, S, { from: isNaN(ei) ? 0 : ei, to: isNaN(ej) ? n - 1 : ej, color: idx, alpha: 0.14 });
      const ps = [{ at: isNaN(ei) ? 0 : ei, name: 'i', color: cl }];
      if (!isNaN(ej)) ps.push({ at: ej, name: 'j', color: cr });
      if (L > 2) ptr(ctx, S, ps);
      else ptr(ctx, S, [{ at: 0, name: 'i', color: cl }]);
      /* the pair-sum table: row i, column j, i < j; a move rules out a whole row (i moves) or a column (j moves) */
      const m = n - 1, cw = Math.min(110, 840 / m), ch = 50, gx = 700 - (m * cw) / 2, gy = 360;
      text(ctx, 'nums[i] + nums[j] for each pair i < j', gx, gy - 66, PAL.muted, { size: 26 });
      for (let c = 1; c < n; c += 1) text(ctx, String(c), gx + (c - 0.5) * cw, gy - 22, c === Jn ? cr : alpha(idx, 0.8), { size: 26, align: 'center', weight: c === Jn ? 600 : 400 });
      text(ctx, 'j', gx + m * cw + 26, gy - 22, cr, { size: 28, weight: 600, italic: true });
      for (let r = 0; r < n - 1; r += 1) {
        text(ctx, String(r), gx - 18, gy + (r + 0.5) * ch, r === I ? cl : alpha(idx, 0.8), { size: 26, align: 'right', weight: r === I ? 600 : 400 });
        for (let c = r + 1; c < n; c += 1) {
          const x0 = gx + (c - 1) * cw, y0 = gy + r * ch, out = r < I || c > Jn, cur = r === I && c === Jn && L >= 6 && L !== 9 && L !== 11 && L !== 13;
          const s = A[r] + A[c];
          rect(ctx, x0, y0, cw, ch, out ? null : alpha(idx, 0.10), out ? alpha(PAL.ink, 0.15) : alpha(PAL.ink, 0.45), 2);
          text(ctx, String(s), x0 + cw / 2, y0 + ch / 2, out ? alpha(key, 0.3) : s === t ? key : alpha(key, 0.8), { size: 26, align: 'center', weight: s === t && !out ? 600 : 400 });
          if (cur) rect(ctx, x0 + 2, y0 + 2, cw - 4, ch - 4, null, found ? key : PAL.ink, 4);
        }
      }
      text(ctx, 'i', gx - 54, gy + ((n - 1) * ch) / 2, cl, { size: 28, weight: 600, italic: true, align: 'right' });
      const checks = v.checks || 0;
      text(ctx, `checks ${checks} ≤ n − 1 = ${n - 1}`, 1340, 770, C('cost'), { size: 28, align: 'right' });
    },
  });
})();

/* ================================================================ sim-three-sum: TheAlgorithms three_sum */
(function () {
  const PY = J([
    'def three_sum(nums: list[int]) -> list[list[int]]:',
    '    nums.sort()',
    '    ans = []',
    '    for i in range(len(nums) - 2):',
    '        if i == 0 or (nums[i] != nums[i - 1]):',
    '            low, high, c = i + 1, len(nums) - 1, 0 - nums[i]',
    '            while low < high:',
    '                if nums[low] + nums[high] == c:',
    '                    ans.append([nums[i], nums[low], nums[high]])',
    '',
    '                    while low < high and nums[low] == nums[low + 1]:',
    '                        low += 1',
    '                    while low < high and nums[high] == nums[high - 1]:',
    '                        high -= 1',
    '',
    '                    low += 1',
    '                    high -= 1',
    '                elif nums[low] + nums[high] < c:',
    '                    low += 1',
    '                else:',
    '                    high -= 1',
    '    return ans',
  ]);
  const body = (o) => J([
    o.head,
    `    ${o.sort}`,
    `    ${o.ans}`,
    `    for (${o.int} i = 0; i < ${o.len} - 2; i++) {`,
    '        if (i == 0 || (nums[i] != nums[i - 1])) {',
    `            ${o.int} low = i + 1, high = ${o.len} - 1, c = 0 - nums[i];`,
    '            while (low < high) {',
    '                if (nums[low] + nums[high] == c) {',
    `                    ${o.add};`,
    '',
    '                    while (low < high && nums[low] == nums[low + 1]) {',
    '                        low += 1;',
    '                    }',
    '                    while (low < high && nums[high] == nums[high - 1]) {',
    '                        high -= 1;',
    '                    }',
    '',
    '                    low += 1;',
    '                    high -= 1;',
    '                } else if (nums[low] + nums[high] < c) {',
    '                    low += 1;',
    '                } else {',
    '                    high -= 1;',
    '                }',
    '            }',
    '        }',
    '    }',
    '    return ans;',
    '}',
  ]);
  const JAVA = body({ head: 'static List<List<Integer>> threeSum(int[] nums) {', sort: 'Arrays.sort(nums);', ans: 'List<List<Integer>> ans = new ArrayList<>();', int: 'int', len: 'nums.length', add: 'ans.add(List.of(nums[i], nums[low], nums[high]))' });
  const CPP = body({ head: 'std::vector<std::vector<int>> threeSum(std::vector<int>& nums) {', sort: 'std::sort(nums.begin(), nums.end());', ans: 'std::vector<std::vector<int>> ans;', int: 'int', len: '(int) nums.size()', add: 'ans.push_back({nums[i], nums[low], nums[high]})' });
  const JS = body({ head: 'function threeSum(nums) {', sort: 'nums.sort((a, b) => a - b);', ans: 'const ans = [];', int: 'let', len: 'nums.length', add: 'ans.push([nums[i], nums[low], nums[high]])' })
    .replace('(i == 0 || (nums[i] != nums[i - 1]))', '(i === 0 || (nums[i] !== nums[i - 1]))').replace('nums[high] == c', 'nums[high] === c')
    .replace('nums[low] == nums[low + 1]', 'nums[low] === nums[low + 1]').replace('nums[high] == nums[high - 1]', 'nums[high] === nums[high - 1]');
  const MAP = lines(22, { 13: 14, 14: 15, 15: 17, 16: 18, 17: 19, 18: 20, 19: 21, 20: 22, 21: 23, 22: 28 });
  const run = (input) => F.trace((at) => {
    const nums = input.slice(), ans = [];
    let checks = 0;
    at(2, { nums, checks }, ['sort']);
    nums.sort((a, b) => a - b); at(2, { nums, checks }, ['sorted']);
    at(3, { nums, ans, checks });
    for (let i = 0; i < nums.length - 2; i += 1) {
      at(4, { nums, i, ans, checks });
      const fresh = i === 0 || nums[i] !== nums[i - 1];
      at(5, { nums, i, ans, checks }, fresh ? ['fresh'] : ['repeat']);
      if (!fresh) continue;
      let low = i + 1, high = nums.length - 1; const c = 0 - nums[i];
      at(6, { nums, i, low, high, c, ans, checks });
      while (low < high) {
        at(7, { nums, i, low, high, c, ans, checks });
        const s = nums[low] + nums[high]; checks += 1;
        at(8, { nums, i, low, high, c, 'nums[low] + nums[high]': s, ans, checks });
        if (s === c) {
          ans.push([nums[i], nums[low], nums[high]]);
          at(9, { nums, i, low, high, c, ans, checks }, ['found']);
          while (low < high && nums[low] === nums[low + 1]) { at(11, { nums, i, low, high, c, ans, checks }); low += 1; at(12, { nums, i, low, high, c, ans, checks }, ['skip']); }
          while (low < high && nums[high] === nums[high - 1]) { at(13, { nums, i, low, high, c, ans, checks }); high -= 1; at(14, { nums, i, low, high, c, ans, checks }, ['skip']); }
          low += 1; at(16, { nums, i, low, high, c, ans, checks });
          high -= 1; at(17, { nums, i, low, high, c, ans, checks });
        } else if (s < c) { at(18, { nums, i, low, high, c, ans, checks }); low += 1; at(19, { nums, i, low, high, c, ans, checks }, ['up']); }
        else { at(20, { nums, i, low, high, c, ans, checks }); high -= 1; at(21, { nums, i, low, high, c, ans, checks }, ['down']); }
      }
    }
    at(22, { nums, ans, checks }, ['done']);
  });
  const INPUTS = [
    { value: 'wiki', label: 'Wikipedia’s example', A: [-25, -10, -7, -3, 2, 4, 8, 10] },
    { value: 'dup', label: 'duplicates', A: [-1, 0, 1, 2, -1, -4] },
    { value: 'none', label: 'no triple', A: [1, 2, 3, 4] },
  ];
  const d = sim('sim-three-sum', 760);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS3,
    lineMap: { java: MAP, cpp: MAP, javascript: MAP },
    blocks: [
      { id: 'sort', lines: [2, 3], label: 'sort the array (a library call)', touches: ['nums'] },
      { id: 'outer', lines: [4, 21], label: 'fix a = nums[i], unless it equals the a before', touches: ['i'] },
      { id: 'pair', lines: [7, 21], label: 'one check of nums[low] + nums[high] against c = −a', touches: ['low', 'high'] },
      { id: 'found', lines: [9, 17], label: 'record the triple, pass over equal neighbours', touches: ['ans', 'low', 'high'] },
    ],
    refs: { i: () => F.ref('ts-i'), low: () => F.ref('ts-start'), high: () => F.ref('ts-end') },
  });
  F.debug(d, {
    code, watch: ['i', 'low', 'high', 'c', 'nums[low] + nums[high]', 'checks'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0];
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const nums = Array.isArray(v.nums) ? v.nums : inp.A, n = nums.length;
      const ci = F.ref('ts-i'), cs = F.ref('ts-start'), ce = F.ref('ts-end'), idx = C('index'), key = C('key');
      const I = typeof v.i === 'number' ? v.i : -1, lo = typeof v.low === 'number' ? v.low : -1, hi = typeof v.high === 'number' ? v.high : -1;
      const ans = Array.isArray(v.ans) ? v.ans : [];
      let head;
      if (ev[0] === 'sort') head = 'First the array is sorted, with the library’s sort.';
      else if (L <= 3) head = `Sorted: ${nums.map(neg).join(', ')}.`;
      else if (L === 4 || L === 5) head = ev[0] === 'repeat' ? `nums[${I}] = ${neg(nums[I])} repeats nums[${I - 1}]: the same a again, passed over.` : `a = nums[${I}] = ${neg(nums[I])}.`;
      else if (L === 6 || L === 7) head = `a = ${neg(nums[I])}: low and high close in on a pair summing to c = ${neg(v.c)}.`;
      else if (L === 8 || L === 18 || L === 20) { const s = nums[lo] + nums[hi]; head = `nums[${lo}] + nums[${hi}] = ${neg(nums[lo])} + ${neg(nums[hi])} = ${neg(s)} ${s === v.c ? '=' : s < v.c ? '<' : '>'} c = ${neg(v.c)}`; }
      else if (L === 9) { const tr = ans[ans.length - 1]; head = `${tr.map(neg).join(' + ')} = 0: a triple.`; }
      else if (L === 19) head = `Too small: low moves right, to ${lo}.`;
      else if (L === 21) head = `Too big: high moves left, to ${hi}.`;
      else if (L >= 11 && L <= 17) head = 'Past the triple: low and high both move on, over any equal neighbours.';
      else head = ans.length ? `Done: ${ans.length} triple${ans.length > 1 ? 's' : ''} sum${ans.length > 1 ? '' : 's'} to 0.` : 'Done: no three numbers sum to 0.';
      topline(ctx, head);
      const S = cells(ctx, { values: nums, y: 230, state: (k) => (I >= 0 && k < I ? 'faded' : k === I ? 'hot' : lo >= 0 && (k < lo || k > hi) && k !== I ? 'faded' : 'live') });
      if (lo >= 0 && hi >= lo) F.ds.region(ctx, S, { from: g.num('low'), to: g.num('high'), color: idx, alpha: 0.14 });
      const ps = [];
      if (I >= 0) ps.push({ at: g.num('i'), name: 'i', color: ci });
      if (lo >= 0) ps.push({ at: g.num('low'), name: 'low', color: cs }, { at: g.num('high'), name: 'high', color: ce });
      if (ps.length) ptr(ctx, S, ps);
      /* a = nums[i] and the pair being tried, as a sum */
      if (I >= 0 && lo >= 0 && L >= 6 && L !== 22) {
        const y = 400;
        text(ctx, `a = ${neg(nums[I])}`, 300, y, ci, { size: 32, weight: 600, align: 'center' });
        text(ctx, `b = ${neg(nums[lo])}`, 640, y, cs, { size: 32, weight: 600, align: 'center' });
        text(ctx, `c = ${neg(nums[hi])}`, 980, y, ce, { size: 32, weight: 600, align: 'center' });
        text(ctx, `a + b + c = ${neg(nums[I] + nums[lo] + nums[hi])}`, 700, y + 56, key, { size: 30, align: 'center' });
      }
      text(ctx, 'triples found', 120, 560, PAL.muted, { size: 26 });
      ans.forEach((tr, k) => text(ctx, `(${tr.map(neg).join(', ')})`, 120 + k * 300, 610, key, { size: 32, weight: 600 }));
      if (!ans.length) text(ctx, '—', 120, 610, PAL.muted, { size: 30 });
      const checks = v.checks || 0, bound = ((n - 1) * (n - 2)) / 2;
      text(ctx, `pair checks ${checks} ≤ (n − 1)(n − 2)/2 = ${bound}`, 1340, 720, C('cost'), { size: 28, align: 'right' });
    },
  });
})();

/* ================================================================ sim-merge: TheAlgorithms merge_sorted_arrays */
(function () {
  const PY = J([
    'def merge_sorted_arrays(nums1: list[int], nums2: list[int]) -> list[int]:',
    '    for nums in (nums1, nums2):',
    '        if list(nums) != sorted(nums):',
    '            msg = f"{nums = } is not sorted"',
    '            raise ValueError(msg)',
    '    # If one array is empty, simply return the other.',
    '    if not nums1:',
    '        return nums2',
    '    if not nums2:',
    '        return nums1',
    '',
    '    # Two-pointer approach to merge both sorted arrays.',
    '    i, j = 0, 0',
    '    merged = []',
    '',
    '    while i < len(nums1) and j < len(nums2):',
    '        if nums1[i] <= nums2[j]:',
    '            merged.append(nums1[i])',
    '            i += 1',
    '        else:',
    '            merged.append(nums2[j])',
    '            j += 1',
    '',
    '    # Append remaining elements if any.',
    '    merged.extend(nums1[i:])',
    '    merged.extend(nums2[j:])',
    '',
    '    return merged',
  ]);
  const JAVA = J([
    'static int[] mergeSortedArrays(int[] nums1, int[] nums2) {',
    '    for (int[] nums : new int[][] {nums1, nums2}) {',
    '        int[] sorted = nums.clone(); Arrays.sort(sorted);',
    '        if (!Arrays.equals(nums, sorted)) {',
    '            String msg = "nums = " + Arrays.toString(nums) + " is not sorted";',
    '            throw new IllegalArgumentException(msg);',
    '        }',
    '    }',
    '    // If one array is empty, simply return the other.',
    '    if (nums1.length == 0) {',
    '        return nums2;',
    '    }',
    '    if (nums2.length == 0) {',
    '        return nums1;',
    '    }',
    '',
    '    // Two-pointer approach to merge both sorted arrays.',
    '    int i = 0, j = 0;',
    '    List<Integer> merged = new ArrayList<>();',
    '',
    '    while (i < nums1.length && j < nums2.length) {',
    '        if (nums1[i] <= nums2[j]) {',
    '            merged.add(nums1[i]);',
    '            i += 1;',
    '        } else {',
    '            merged.add(nums2[j]);',
    '            j += 1;',
    '        }',
    '    }',
    '',
    '    // Append remaining elements if any.',
    '    while (i < nums1.length) merged.add(nums1[i++]);',
    '    while (j < nums2.length) merged.add(nums2[j++]);',
    '',
    '    return merged.stream().mapToInt(Integer::intValue).toArray();',
    '}',
  ]);
  const braced = (o) => J([
    o.head,
    `    for (${o.each}) {`,
    `        if (${o.unsorted}) {`,
    `            ${o.msg}`,
    `            ${o.raise}`,
    '        }',
    '    }',
    '    // If one array is empty, simply return the other.',
    `    if (${o.empty1}) {`,
    '        return nums2;',
    '    }',
    `    if (${o.empty2}) {`,
    '        return nums1;',
    '    }',
    '',
    '    // Two-pointer approach to merge both sorted arrays.',
    `    ${o.ij}`,
    `    ${o.merged}`,
    '',
    `    while (i < ${o.len1} && j < ${o.len2}) {`,
    '        if (nums1[i] <= nums2[j]) {',
    `            merged.${o.push}(nums1[i]);`,
    '            i += 1;',
    '        } else {',
    `            merged.${o.push}(nums2[j]);`,
    '            j += 1;',
    '        }',
    '    }',
    '',
    '    // Append remaining elements if any.',
    `    ${o.rest1}`,
    `    ${o.rest2}`,
    '',
    '    return merged;',
    '}',
  ]);
  const CPP = braced({
    head: 'std::vector<int> mergeSortedArrays(const std::vector<int>& nums1, const std::vector<int>& nums2) {',
    each: 'const auto& nums : {nums1, nums2}', unsorted: '!std::is_sorted(nums.begin(), nums.end())',
    msg: 'std::string msg = "nums is not sorted";', raise: 'throw std::invalid_argument(msg);',
    empty1: 'nums1.empty()', empty2: 'nums2.empty()', ij: 'size_t i = 0, j = 0;', merged: 'std::vector<int> merged;',
    len1: 'nums1.size()', len2: 'nums2.size()', push: 'push_back',
    rest1: 'merged.insert(merged.end(), nums1.begin() + i, nums1.end());', rest2: 'merged.insert(merged.end(), nums2.begin() + j, nums2.end());',
  });
  const JS = braced({
    head: 'function mergeSortedArrays(nums1, nums2) {',
    each: 'const nums of [nums1, nums2]', unsorted: 'nums.some((x, k) => k > 0 && nums[k - 1] > x)',
    msg: 'const msg = `nums = [${nums}] is not sorted`;', raise: 'throw new RangeError(msg);',
    empty1: 'nums1.length === 0', empty2: 'nums2.length === 0', ij: 'let i = 0, j = 0;', merged: 'const merged = [];',
    len1: 'nums1.length', len2: 'nums2.length', push: 'push',
    rest1: 'merged.push(...nums1.slice(i));', rest2: 'merged.push(...nums2.slice(j));',
  });
  const MAPJ = { 1: 1, 2: 2, 3: [3, 4], 4: 5, 5: 6, 6: 9, 7: 10, 8: 11, 9: 13, 10: 14, 11: 16, 12: 17, 13: 18, 14: 19, 15: 20, 16: 21, 17: 22, 18: 23, 19: 24, 20: 25, 21: 26, 22: 27, 23: 30, 24: 31, 25: 32, 26: 33, 27: 34, 28: 35 };
  const MAPC = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 8, 7: 9, 8: 10, 9: 12, 10: 13, 11: 15, 12: 16, 13: 17, 14: 18, 15: 19, 16: 20, 17: 21, 18: 22, 19: 23, 20: 24, 21: 25, 22: 26, 23: 29, 24: 30, 25: 31, 26: 32, 27: 33, 28: 34 };
  const run = (A, B) => F.trace((at) => {
    let comps = 0;
    for (const nums of [A, B]) { at(2, { nums, comps }); at(3, { nums, comps }); }
    at(7, { comps });
    if (!A.length) { at(8, { merged: B, comps }, ['returnB']); return; }
    at(9, { comps });
    if (!B.length) { at(10, { merged: A, comps }, ['returnA']); return; }
    let i = 0, j = 0; at(13, { i, j, comps });
    const merged = []; at(14, { i, j, merged, comps });
    while (i < A.length && j < B.length) {
      at(16, { i, j, merged, comps });
      comps += 1;
      at(17, { i, j, merged, comps, 'nums1[i]': A[i], 'nums2[j]': B[j] });
      if (A[i] <= B[j]) { merged.push(A[i]); at(18, { i, j, merged, comps }, ['takeA', i]); i += 1; at(19, { i, j, merged, comps }); }
      else { at(20, { i, j, merged, comps }); merged.push(B[j]); at(21, { i, j, merged, comps }, ['takeB', j]); j += 1; at(22, { i, j, merged, comps }); }
    }
    const a0 = merged.length; merged.push(...A.slice(i)); at(25, { i, j, merged, comps }, ['restA', a0]);
    const b0 = merged.length; merged.push(...B.slice(j)); at(26, { i, j, merged, comps }, ['restB', b0]);
    at(28, { i, j, merged, comps }, ['done']);
  });
  const INPUTS = [
    { value: 'mix', label: 'interleaved', A: [1, 4, 7, 9], B: [2, 3, 5, 10, 12] },
    { value: 'first', label: 'A runs out first', A: [1, 2, 3], B: [4, 5, 6] },
    { value: 'ties', label: 'equal keys', A: [2, 2, 5], B: [2, 3] },
    { value: 'empty', label: 'B empty', A: [1, 3], B: [] },
  ];
  const d = sim('sim-merge', 720);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS }, ai: AIS3,
    lineMap: { java: MAPJ, cpp: MAPC, javascript: MAPC },
    blocks: [
      { id: 'check', lines: [2, 5], label: 'check that both inputs are sorted', touches: ['nums'] },
      { id: 'empty', lines: [7, 10], label: 'if one input is empty, return the other', touches: ['merged'] },
      { id: 'init', lines: [13, 14], label: 'start at both heads, with C empty', touches: ['i', 'j', 'merged'] },
      { id: 'take', lines: [16, 22], label: 'append the smaller head to C and drop it', touches: ['i', 'j', 'merged'] },
      { id: 'rest', lines: [25, 26], label: 'append what is left of either list', touches: ['merged'] },
    ],
    refs: { nums1: () => F.ref('list-a'), i: () => F.ref('list-a'), nums2: () => F.ref('list-b'), j: () => F.ref('list-b'), merged: () => F.ref('list-c') },
  });
  F.debug(d, {
    code, watch: ['i', 'j', 'merged', 'comps'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, x.B) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, B = inp.B, N = A.length + B.length;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const ca = F.ref('list-a'), cb = F.ref('list-b'), cc = F.ref('list-c'), idx = C('index'), key = C('key');
      const i = typeof v.i === 'number' ? v.i : 0, j = typeof v.j === 'number' ? v.j : 0;
      const merged = Array.isArray(v.merged) ? v.merged : [];
      let head;
      if (L <= 3) head = 'Both inputs are checked: each must already be sorted.';
      else if (ev[0] === 'returnA' || ev[0] === 'returnB') head = `${ev[0] === 'returnA' ? 'B' : 'A'} is empty, so the other list is the answer as it stands.`;
      else if (L <= 14) head = 'Both heads are the first elements; C starts empty.';
      else if (L === 16) head = `C holds ${merged.length} element${merged.length === 1 ? '' : 's'}, in order; the two heads are next.`;
      else if (L === 17 || L === 20) head = `head(A) = ${A[i]} ${A[i] <= B[j] ? '≤' : '>'} head(B) = ${B[j]}`;
      else if (ev[0] === 'takeA' || L === 19) head = `head(A) = ${A[ev[0] === 'takeA' ? ev[1] : i - 1]} goes to C and is dropped from A.`;
      else if (ev[0] === 'takeB' || L === 22) head = `head(B) = ${B[ev[0] === 'takeB' ? ev[1] : j - 1]} goes to C and is dropped from B.`;
      else if (L === 25 || L === 26) head = 'One list is empty: the rest of the other is copied to C as it is.';
      else head = `C is A and B merged: ${N} elements in order after ${v.comps} comparison${v.comps === 1 ? '' : 's'}.`;
      topline(ctx, head);
      const cell = Math.min(100, 1000 / Math.max(N, 1)), x0 = 220;
      const SA = cells(ctx, { values: A, y: 200, cell, x0, name: 'A', nameColor: ca, state: (k) => (k < i || (L >= 25 && L <= 28 && ev[0] !== 'returnA') ? 'faded' : k === i && L >= 13 ? 'hot' : 'live'), index: true });
      const SB = cells(ctx, { values: B.length ? B : [], y: 350, cell, x0, name: 'B', nameColor: cb, state: (k) => (k < j || (L >= 26 && L <= 28 && ev[0] !== 'returnB') ? 'faded' : k === j && L >= 13 ? 'hot' : 'live') });
      if (!B.length) text(ctx, '(empty)', x0 + 10, 350, PAL.muted, { size: 28 });
      if (L >= 13 && L <= 22) {
        if (i < A.length) ptr(ctx, SA, [{ at: g.num('i'), name: 'i', color: ca }]);
        if (j < B.length) ptr(ctx, SB, [{ at: g.num('j'), name: 'j', color: cb }]);
      }
      /* C: the merged prefix is sorted and holds exactly A[0..i) and B[0..j) */
      const out = ev[0] === 'returnA' ? A : ev[0] === 'returnB' ? B : merged;
      const shown = out.length ? out : [];
      const SC = cells(ctx, { values: shown.concat(new Array(Math.max(0, N - shown.length)).fill('')), y: 540, cell, x0, name: 'C', nameColor: cc, state: (k) => (k < shown.length ? 'live' : 'hollow') });
      if (shown.length) F.ds.region(ctx, SC, { from: 0, to: shown.length - 1, color: idx, alpha: 0.14 });
      /* the head just taken travels down into C */
      if ((ev[0] === 'takeA' || ev[0] === 'takeB') && g.k < 1) {
        const from = ev[0] === 'takeA' ? SA : SB, k0 = ev[1], to = merged.length - 1;
        const fx = from.x(k0), fy = from.y, tx = SC.x(to), ty = SC.y, e = g.k;
        arrow(ctx, fx, fy + 40, tx, ty - 40, ev[0] === 'takeA' ? ca : cb, 4);
        text(ctx, String(merged[to]), fx + (tx - fx) * e, fy + (ty - fy) * e, key, { size: 32, align: 'center', weight: 600 });
      }
      text(ctx, `C sorted, holding A[0..${i}) and B[0..${j})`, x0, 640, idx, { size: 26 });
      text(ctx, `comparisons ${v.comps || 0} ≤ m + n − 1 = ${Math.max(0, N - 1)}`, 1340, 690, C('cost'), { size: 28, align: 'right' });
    },
  });
})();

/* ================================================================ sim-moving-window: the simple moving average */
(function () {
  /* an invented series of 24 closing prices (the source names stock prices and gives none) */
  const P = [12, 13, 12, 14, 15, 17, 16, 18, 17, 19, 21, 20, 22, 21, 23, 25, 24, 23, 25, 27, 26, 28, 27, 29];
  const N = P.length;
  const d = sim('sim-moving-window', 620);
  const sK = ctl(d.controls, { label: 'k', cls: 'size', key: 'k', min: 2, max: 8, step: 1, value: 4, unit: '', dec: 0, onInput: () => cy.reset() });
  /* the window's end runs from k + 1 to N, one step per new data point; the first window is the starting state */
  const cy = cycle(() => N - Math.round(sK.v), 1.2);
  const f2 = (x) => x.toFixed(2);
  const mean = (a, b) => { let s = 0; for (let q = a; q <= b; q += 1) s += P[q - 1]; return s / (b - a + 1); };
  function draw() {
    const { ctx } = begin(d.c);
    const k = Math.round(sK.v), tau = cy.now(), step = Math.floor(tau), frac = Math.min(1, tau - step);
    const e = Math.min(N, k + step), moving = e < N && frac > 0;
    const ease = moving ? F.ease.smooth(frac) : 0;
    const prev = mean(e - k + 1, e), nextE = Math.min(N, e + 1);
    const box = { l: 110, r: 1340, t: 130, b: 470 }, bw = (box.r - box.l) / N;
    const Y = (p) => box.b - ((p - 8) / (32 - 8)) * (box.b - box.t);
    const X = (q) => box.l + (q - 0.5) * bw;
    const key = C('key'), idx = C('index'), size = C('size');
    /* the window [e − k + 1, e], sliding toward [e − k + 2, e + 1] */
    const wl = box.l + (e - k + ease) * bw, wr = box.l + (e + ease) * bw;
    rect(ctx, wl, box.t - 10, wr - wl, box.b - box.t + 10, alpha(idx, 0.12));
    F.hbracket(ctx, wl + 4, wr - 4, box.t - 24, size, `k = ${k}`, { side: 'above' });
    for (let q = 1; q <= N; q += 1) {
      const inWin = q >= e - k + 1 && q <= e, entering = moving && q === e + 1, leaving = moving && q === e - k + 1;
      const c = inWin || entering ? key : alpha(key, 0.35);
      rect(ctx, X(q) - bw * 0.32, Y(P[q - 1]), bw * 0.64, box.b - Y(P[q - 1]), alpha(c, leaving ? 0.25 + 0.6 * (1 - ease) : entering ? 0.25 + 0.6 * ease : inWin ? 0.85 : 0.35));
      if (q % 2 === 1 || bw > 60) text(ctx, String(q), X(q), box.b + 26, PAL.muted, { size: 26, align: 'center' });
    }
    line(ctx, box.l, box.b, box.r, box.b, PAL.ink, 2);
    text(ctx, 'p', box.l - 60, box.t + 20, key, { size: 32, italic: true, weight: 600 });
    text(ctx, 'data point', box.r, box.b + 62, PAL.muted, { size: 26, align: 'right' });
    /* the SMA so far, one point per window end, dashed as an average */
    ctx.save(); ctx.strokeStyle = key; ctx.lineWidth = 4; ctx.setLineDash([10, 10]); ctx.beginPath();
    for (let q = k; q <= e; q += 1) { const y = Y(mean(q - k + 1, q)); if (q === k) ctx.moveTo(X(q), y); else ctx.lineTo(X(q), y); }
    ctx.stroke(); ctx.restore();
    for (let q = k; q <= e; q += 1) F.dot(ctx, X(q), Y(mean(q - k + 1, q)), key, q === e, q === e ? 9 : 6);
    if (e < N) {
      const pin = P[nextE - 1], pout = P[e - k], next = prev + (pin - pout) / k;
      topline(ctx, `SMA = ${f2(prev)} + (${pin} − ${pout})/${k} = ${f2(next)}`);
      tex(d.readout, `\\textit{SMA}_{k,\\text{next}} = \\textit{SMA}_{k,\\text{prev}} + \\frac{p_{n+1} - p_{n-k+1}}{k} \\\\ ${f2(next)} = ${f2(prev)} + \\frac{${pin} - ${pout}}{${k}}`);
      if (moving) { arrow(ctx, X(e + 1), Y(pin) - 60, X(e + 1), Y(pin) - 12, key, 4); }
    } else {
      topline(ctx, `The last window: SMA = ${f2(prev)}, the mean of the last ${k} data points.`);
      tex(d.readout, `\\textit{SMA}_{k} = \\frac{1}{k} \\sum_{i=n-k+1}^{n} p_{i} = ${f2(prev)}`);
    }
    text(ctx, `arithmetic steps per move 3, against k = ${k} additions to sum the window again`, 1340, 590, C('cost'), { size: 26, align: 'right' });
  }
  register(d.fig, { update: (dt) => cy.step(dt, () => 1 / 1.4), draw });
})();

/* ================================================================ sim-variable-window: doocs 0713 */
(function () {
  const PY = J([
    'class Solution:',
    '    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:',
    '        ans = l = 0',
    '        p = 1',
    '        for r, x in enumerate(nums):',
    '            p *= x',
    '            while l <= r and p >= k:',
    '                p //= nums[l]',
    '                l += 1',
    '            ans += r - l + 1',
    '        return ans',
  ]);
  const JAVA = J([
    'class Solution {',
    '    public int numSubarrayProductLessThanK(int[] nums, int k) {',
    '        int ans = 0, l = 0;',
    '        int p = 1;',
    '        for (int r = 0; r < nums.length; ++r) {',
    '            p *= nums[r];',
    '            while (l <= r && p >= k) {',
    '                p /= nums[l++];',
    '            }',
    '            ans += r - l + 1;',
    '        }',
    '        return ans;',
    '    }',
    '}',
  ]);
  const CPP = J([
    'class Solution {',
    'public:',
    '    int numSubarrayProductLessThanK(vector<int>& nums, int k) {',
    '        int ans = 0, l = 0;',
    '        int p = 1;',
    '        for (int r = 0; r < nums.size(); ++r) {',
    '            p *= nums[r];',
    '            while (l <= r && p >= k) {',
    '                p /= nums[l++];',
    '            }',
    '            ans += r - l + 1;',
    '        }',
    '        return ans;',
    '    }',
    '};',
  ]);
  const JS = J([
    '/**',
    ' * @param {number[]} nums',
    ' * @param {number} k',
    ' * @return {number}',
    ' */',
    'var numSubarrayProductLessThanK = function (nums, k) {',
    '    const n = nums.length;',
    '    let [ans, l, p] = [0, 0, 1];',
    '    for (let r = 0; r < n; ++r) {',
    '        p *= nums[r];',
    '        while (l <= r && p >= k) {',
    '            p /= nums[l++];',
    '        }',
    '        ans += r - l + 1;',
    '    }',
    '    return ans;',
    '};',
  ]);
  const MAPJ = { 1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 8, 10: 10, 11: 12 };
  const MAPC = { 1: 1, 2: 3, 3: 4, 4: 5, 5: 6, 6: 7, 7: 8, 8: 9, 9: 9, 10: 11, 11: 13 };
  const MAPS = { 1: 6, 2: 6, 3: 8, 4: 8, 5: 9, 6: 10, 7: 11, 8: 12, 9: 12, 10: 14, 11: 16 };
  const run = (nums, k) => F.trace((at) => {
    let ans = 0, l = 0, moves = 0; at(3, { l, ans, k, moves });
    let p = 1; at(4, { l, p, ans, k, moves });
    for (let r = 0; r < nums.length; r += 1) {
      const x = nums[r]; moves += 1;
      at(5, { r, x, l, p, ans, k, moves });
      p *= x; at(6, { r, x, l, p, ans, k, moves }, ['extend']);
      while (l <= r && p >= k) {
        at(7, { r, x, l, p, ans, k, moves });
        p = Math.floor(p / nums[l]); at(8, { r, x, l, p, ans, k, moves }, ['drop', l]);
        l += 1; moves += 1; at(9, { r, x, l, p, ans, k, moves });
      }
      ans += r - l + 1; at(10, { r, x, l, p, ans, k, moves }, ['count', r - l + 1]);
    }
    at(11, { l, p, ans, k, moves }, ['done']);
  });
  const INPUTS = [
    { value: 'typ', label: 'typical', A: [3, 2, 5, 1, 4, 2, 6], k: 20 },
    { value: 'k1', label: 'k = 1', A: [3, 2, 5, 1, 4, 2, 6], k: 1 },
    { value: 'ones', label: 'never shrinks', A: [1, 2, 1, 1, 2, 1, 1], k: 100 },
    { value: 'big', label: 'one element too big', A: [2, 9, 30, 1, 3], k: 10 },
  ];
  const d = sim('sim-variable-window', 700);
  const code = F.code(d, {
    src: { python: PY, java: JAVA, cpp: CPP, javascript: JS },
    lineMap: { java: MAPJ, cpp: MAPC, javascript: MAPS },
    blocks: [
      { id: 'init', lines: [3, 4], label: 'an empty window, with product 1', touches: ['l', 'p'] },
      { id: 'step', lines: [5, 10], label: 'one more element on the right', touches: ['r'] },
      { id: 'extend', lines: [6, 6], label: 'take x = nums[r] into the product', touches: ['r', 'p'] },
      { id: 'shrink', lines: [7, 9], label: 'while p ≥ k, drop nums[l] from the left', touches: ['l', 'p'] },
      { id: 'count', lines: [10, 10], label: 'count the r − l + 1 windows that end at r', touches: ['ans'] },
    ],
    refs: { l: () => F.ref('win-l'), r: () => F.ref('win-r'), p: () => F.ref('win-tmp') },
  });
  F.debug(d, {
    code, watch: ['r', 'x', 'l', 'p', 'k', 'ans', 'moves'],
    inputs: INPUTS.map((x) => ({ value: x.value, label: x.label, trace: run(x.A, x.k) })),
    draw: (g) => {
      const ctx = g.ctx; if (!ctx) return;
      const inp = INPUTS.find((x) => x.value === g.input) || INPUTS[0], A = inp.A, n = A.length, k = inp.k;
      const v = g.frame.vars, L = g.frame.line, ev = g.frame.ev || [];
      const cl = F.ref('win-l'), cr = F.ref('win-r'), cp = F.ref('win-tmp'), idx = C('index'), key = C('key');
      const l = typeof v.l === 'number' ? v.l : 0, r = typeof v.r === 'number' ? v.r : -1, p = typeof v.p === 'number' ? v.p : 1;
      let head;
      if (L <= 4) head = `An empty window, product 1, and k = ${k}.`;
      else if (L === 5) head = `r = ${r}: x = ${A[r]} joins the window on the right.`;
      else if (L === 6) head = p >= k ? `p = ${p} ≥ ${k}: the window must shrink from the left.` : `p = ${p} < ${k}: the window [${l}, ${r}] qualifies.`;
      else if (L === 7 || L === 8 || L === 9) head = `p ≥ k: nums[${ev[0] === 'drop' ? ev[1] : l - 1}] leaves on the left; p = ${p}.`;
      else if (L === 10) head = r < l ? `No window ending at r = ${r} qualifies: r − l + 1 = 0.` : `${r - l + 1} window${r - l + 1 === 1 ? '' : 's'} end at r = ${r}: [${l}, ${r}] and every window inside it that ends at ${r}.`;
      else head = `Done: ${v.ans} windows have product < ${k}.`;
      topline(ctx, head);
      const S = cells(ctx, { values: A, y: 230, state: (q) => (q < l ? 'faded' : q > r ? 'hollow' : 'live') });
      if (r >= l && r >= 0) F.ds.region(ctx, S, { from: Math.max(0, g.num('l')), to: g.num('r'), color: idx, alpha: 0.16 });
      const ps = [{ at: g.num('l'), name: 'l', color: cl }];
      if (r >= 0) ps.push({ at: g.num('r'), name: 'r', color: cr });
      ptr(ctx, S, ps);
      /* the product of the window, written out, against k */
      const inside = r >= l ? A.slice(l, r + 1) : [];
      const prodText = inside.length ? `${inside.join(' · ')} = ${p}` : '1 (empty)';
      text(ctx, `p = ${prodText}`, 120, 370, cp, { size: 32, weight: 600 });
      text(ctx, `${p < k ? '<' : '≥'} k = ${k}`, 120 + F.measure(ctx, `p = ${prodText}`, { size: 32, weight: 600 }) + 20, 370, p < k ? key : C('cost'), { size: 32 });
      /* at a count, the windows that end at r, one bracket each */
      if (L === 10 && r >= l) {
        for (let s = l; s <= r; s += 1) {
          const y = 430 + (s - l) * 30;
          line(ctx, S.x(s) - S.cell * 0.42, y, S.x(r) + S.cell * 0.42, y, alpha(cr, 0.8), 4);
        }
      }
      text(ctx, `windows counted ans = ${v.ans}`, 120, 640, PAL.ink, { size: 28 });
      text(ctx, `pointer moves ${v.moves} ≤ 2n = ${2 * n}`, 1340, 680, C('cost'), { size: 28, align: 'right' });
    },
  });
})();
};
