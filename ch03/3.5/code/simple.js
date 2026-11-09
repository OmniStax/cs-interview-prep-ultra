function delim(c) {
    return c === ' ';
}

function is_op(c) {
    return c === '+' || c === '-' || c === '*' || c === '/';
}

function priority(op) {
    if (op === '+' || op === '-')
        return 1;
    if (op === '*' || op === '/')
        return 2;
    return -1;
}

function process_op(st, op) {
    const r = st.pop();
    const l = st.pop();
    switch (op) {
        case '+': st.push(l + r); break;
        case '-': st.push(l - r); break;
        case '*': st.push(l * r); break;
        case '/': st.push(Math.trunc(l / r)); break;
    }
}

function evaluate(s) {
    const st = [];
    const op = [];
    for (let i = 0; i < s.length; i++) {
        if (delim(s[i]))
            continue;

        if (s[i] === '(') {
            op.push('(');
        } else if (s[i] === ')') {
            while (op[op.length - 1] !== '(') {
                process_op(st, op[op.length - 1]);
                op.pop();
            }
            op.pop();
        } else if (is_op(s[i])) {
            const cur_op = s[i];
            while (op.length > 0 && priority(op[op.length - 1]) >= priority(cur_op)) {
                process_op(st, op[op.length - 1]);
                op.pop();
            }
            op.push(cur_op);
        } else {
            let number = 0;
            while (i < s.length && /[0-9A-Za-z]/.test(s[i]))
                number = number * 10 + s.charCodeAt(i++) - 48;
            --i;
            st.push(number);
        }
    }

    while (op.length > 0) {
        process_op(st, op[op.length - 1]);
        op.pop();
    }
    return st[st.length - 1];
}
