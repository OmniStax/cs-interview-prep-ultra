class StackUnderflowError extends Error {
  constructor(message) { super(message); this.name = 'StackUnderflowError'; }
}
class ZeroDivisionError extends Error {
  constructor(message) { super(message); this.name = 'ZeroDivisionError'; }
}
class ValueError extends Error {
  constructor(message) { super(message); this.name = 'ValueError'; }
}

const isNumber = (w) => /^-?\d+$/.test(w);

function evaluate(instructions) {
  const defs = new Map();
  const stack = [];
  const need = (k) => { if (stack.length < k) throw new StackUnderflowError('Insufficient number of items in stack'); };
  // a definition is expanded when it is made, so a later redefinition does not change it
  const expand = (words) => words.flatMap((w) => defs.get(w) || [w]);
  for (const line of instructions) {
    const words = line.toLowerCase().split(/\s+/).filter(Boolean);
    if (words[0] === ':') {
      const name = words[1];
      if (isNumber(name)) throw new ValueError('illegal operation');
      defs.set(name, expand(words.slice(2, -1)));
      continue;
    }
    for (const w of expand(words)) {
      if (isNumber(w)) { stack.push(Number(w)); continue; }
      switch (w) {
        case '+': need(2); stack.push(stack.pop() + stack.pop()); break;
        case '-': { need(2); const b = stack.pop(); stack.push(stack.pop() - b); break; }
        case '*': need(2); stack.push(stack.pop() * stack.pop()); break;
        case '/': {
          need(2);
          const b = stack.pop();
          if (b === 0) throw new ZeroDivisionError('divide by zero');
          stack.push(Math.trunc(stack.pop() / b));
          break;
        }
        case 'dup': need(1); stack.push(stack[stack.length - 1]); break;
        case 'drop': need(1); stack.pop(); break;
        case 'swap': { need(2); const b = stack.pop(), a = stack.pop(); stack.push(b, a); break; }
        case 'over': need(2); stack.push(stack[stack.length - 2]); break;
        default: throw new ValueError('undefined operation');
      }
    }
  }
  return stack;
}
