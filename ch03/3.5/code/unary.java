static boolean delim(char c) {
    return c == ' ';
}

static boolean is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

static boolean is_unary(String c) {
    return c.equals("+") || c.equals("-");
}

static int priority(String op) {
    if (op.startsWith("u")) // unary operator
        return 3;
    if (op.equals("+") || op.equals("-"))
        return 1;
    if (op.equals("*") || op.equals("/"))
        return 2;
    return -1;
}

static void process_op(Deque<Integer> st, String op) {
    if (op.startsWith("u")) {
        int l = st.pop();
        switch (op.charAt(1)) {
            case '+': st.push(l); break;
            case '-': st.push(-l); break;
        }
    } else {
        int r = st.pop();
        int l = st.pop();
        switch (op.charAt(0)) {
            case '+': st.push(l + r); break;
            case '-': st.push(l - r); break;
            case '*': st.push(l * r); break;
            case '/': st.push(l / r); break;
        }
    }
}

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
                    (!cur_op.startsWith("u") && priority(op.peek()) >= priority(cur_op)) ||
                    (cur_op.startsWith("u") && priority(op.peek()) > priority(cur_op))
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
