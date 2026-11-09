const fs = require('fs');

const priority = (op) => (op[0] === 'u' ? 3 : op === '+' || op === '-' ? 1 : 2);

function processOp(st, op) {
  if (op[0] === 'u') {
    const l = st.pop();
    st.push(op === 'u-' ? -l : l);
  } else {
    const r = st.pop(), l = st.pop();
    st.push(op === '+' ? l + r : op === '-' ? l - r : op === '*' ? l * r : l / r);
  }
}

// two stacks, as cp-algorithms evaluates an expression: numbers on st, operators and brackets on op
function evaluate(s) {
  const st = [], op = [];
  let mayBeUnary = true;
  for (let i = 0; i < s.length; i++) {
    const c = s[i];
    if (/\s/.test(c)) continue;
    if (c === '(') {
      op.push('(');
      mayBeUnary = true;
    } else if (c === ')') {
      while (op[op.length - 1] !== '(') processOp(st, op.pop());
      op.pop();
      mayBeUnary = false;
    } else if ('+-*/'.includes(c)) {
      const cur = mayBeUnary && (c === '+' || c === '-') ? 'u' + c : c;
      while (op.length && op[op.length - 1] !== '(' &&
             (cur[0] === 'u' ? priority(op[op.length - 1]) > priority(cur) : priority(op[op.length - 1]) >= priority(cur))) {
        processOp(st, op.pop());
      }
      op.push(cur);
      mayBeUnary = true;
    } else {
      let j = i;
      while (j < s.length && s[j] >= '0' && s[j] <= '9') j++;
      st.push(Number(s.slice(i, j)));
      i = j - 1;
      mayBeUnary = false;
    }
  }
  while (op.length) processOp(st, op.pop());
  return st[st.length - 1];
}

const out = [];
for (const line of fs.readFileSync(0, 'utf8').split('\n')) {
  if (!line.trim()) continue;
  const v = evaluate(line).toFixed(2);
  out.push(v === '-0.00' ? '0.00' : v);
}
console.log(out.join('\n'));
