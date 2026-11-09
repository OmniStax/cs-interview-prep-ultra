static boolean delim(char c) {
    return c == ' ';
}

static boolean is_op(char c) {
    return c == '+' || c == '-' || c == '*' || c == '/';
}

static int priority(char op) {
    if (op == '+' || op == '-')
        return 1;
    if (op == '*' || op == '/')
        return 2;
    return -1;
}

static void process_op(Deque<Integer> st, char op) {
    int r = st.pop();
    int l = st.pop();
    switch (op) {
        case '+': st.push(l + r); break;
        case '-': st.push(l - r); break;
        case '*': st.push(l * r); break;
        case '/': st.push(l / r); break;
    }
}

static int evaluate(String s) {
    Deque<Integer> st = new ArrayDeque<>();
    Deque<Character> op = new ArrayDeque<>();
    for (int i = 0; i < s.length(); i++) {
        if (delim(s.charAt(i)))
            continue;

        if (s.charAt(i) == '(') {
            op.push('(');
        } else if (s.charAt(i) == ')') {
            while (op.peek() != '(') {
                process_op(st, op.peek());
                op.pop();
            }
            op.pop();
        } else if (is_op(s.charAt(i))) {
            char cur_op = s.charAt(i);
            while (!op.isEmpty() && priority(op.peek()) >= priority(cur_op)) {
                process_op(st, op.peek());
                op.pop();
            }
            op.push(cur_op);
        } else {
            int number = 0;
            while (i < s.length() && Character.isLetterOrDigit(s.charAt(i)))
                number = number * 10 + s.charAt(i++) - '0';
            --i;
            st.push(number);
        }
    }

    while (!op.isEmpty()) {
        process_op(st, op.peek());
        op.pop();
    }
    return st.peek();
}
