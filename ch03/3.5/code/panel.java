static int evaluate(String s) {
    Deque<Integer> st = new ArrayDeque<>();
    Deque<String> op = new ArrayDeque<>();
    boolean may_be_unary = true;
    for (int i = 0; i < s.length(); i++) {
        if (delim(s.charAt(i)))
            continue;

        if (s.charAt(i) == '(') {
            op.push("(");
            may_be_unary = true;
        } else if (s.charAt(i) == ')') {
            while (!op.peek().equals("(")) {
                process_op(st, op.peek());
                op.pop();
            }
            op.pop();
            may_be_unary = false;
        } else if (is_op(s.charAt(i))) {
            String cur_op = String.valueOf(s.charAt(i));
            if (may_be_unary && is_unary(cur_op))
                cur_op = "u" + cur_op;
            while (!op.isEmpty() && (
                    (left_assoc(cur_op) && priority(op.peek()) >= priority(cur_op)) ||
                    (!left_assoc(cur_op) && priority(op.peek()) > priority(cur_op))
                )) {
                process_op(st, op.peek());
                op.pop();
            }
            op.push(cur_op);
            may_be_unary = true;
        } else {
            int number = 0;
            while (i < s.length() && Character.isLetterOrDigit(s.charAt(i)))
                number = number * 10 + s.charAt(i++) - '0';
            --i;
            st.push(number);
            may_be_unary = false;
        }
    }

    while (!op.isEmpty()) {
        process_op(st, op.peek());
        op.pop();
    }
    return st.peek();
}
