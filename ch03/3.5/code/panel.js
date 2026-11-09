function evaluate(s) {
    const st = [];
    const op = [];
    let may_be_unary = true;
    for (let i = 0; i < s.length; i++) {
        if (delim(s[i]))
            continue;

        if (s[i] === '(') {
            op.push('(');
            may_be_unary = true;
        } else if (s[i] === ')') {
            while (op[op.length - 1] !== '(') {
                process_op(st, op[op.length - 1]);
                op.pop();
            }
            op.pop();
            may_be_unary = false;
        } else if (is_op(s[i])) {
            let cur_op = s[i];
            if (may_be_unary && is_unary(cur_op))
                cur_op = 'u' + cur_op;
            while (op.length > 0 && (
                    (left_assoc(cur_op) && priority(op[op.length - 1]) >= priority(cur_op)) ||
                    (!left_assoc(cur_op) && priority(op[op.length - 1]) > priority(cur_op))
                )) {
                process_op(st, op[op.length - 1]);
                op.pop();
            }
            op.push(cur_op);
            may_be_unary = true;
        } else {
            let number = 0;
            while (i < s.length && /[0-9A-Za-z]/.test(s[i]))
                number = number * 10 + s.charCodeAt(i++) - 48;
            --i;
            st.push(number);
            may_be_unary = false;
        }
    }

    while (op.length > 0) {
        process_op(st, op[op.length - 1]);
        op.pop();
    }
    return st[st.length - 1];
}
