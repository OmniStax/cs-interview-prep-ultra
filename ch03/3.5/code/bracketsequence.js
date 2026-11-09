const fs = require('fs');
const MOD = 1000000007n;
const data = fs.readFileSync(0, 'utf8').split(/\s+/).filter(Boolean);
const n = Number(data[0]);
// one running value per open bracket; at an even depth it is a sum, at an odd depth a product
const stack = [0n];
for (const t of data.slice(1, 1 + n)) {
  if (t === '(') {
    stack.push(stack.length % 2 === 1 ? 1n : 0n);
  } else {
    const v = t === ')' ? stack.pop() : BigInt(t);
    const top = stack.length - 1;
    stack[top] = stack.length % 2 === 0 ? (stack[top] * v) % MOD : (stack[top] + v) % MOD;
  }
}
console.log(String(stack[0]));
