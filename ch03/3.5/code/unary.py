def delim(c):
    return c == ' '


def is_op(c):
    return c == '+' or c == '-' or c == '*' or c == '/'


def is_unary(c):
    return c == '+' or c == '-'


def priority(op):
    if op[0] == 'u':  # unary operator
        return 3
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return -1


def process_op(st, op):
    if op[0] == 'u':
        l = st.pop()
        if op[1] == '+':
            st.append(l)
        elif op[1] == '-':
            st.append(-l)
    else:
        r = st.pop()
        l = st.pop()
        if op == '+':
            st.append(l + r)
        elif op == '-':
            st.append(l - r)
        elif op == '*':
            st.append(l * r)
        elif op == '/':
            st.append(int(l / r))


def evaluate(s):
    st = []
    op = []
    may_be_unary = True
    i = 0
    while i < len(s):
        if delim(s[i]):
            i += 1
            continue

        if s[i] == '(':
            op.append('(')
            may_be_unary = True
        elif s[i] == ')':
            while op[-1] != '(':
                process_op(st, op[-1])
                op.pop()
            op.pop()
            may_be_unary = False
        elif is_op(s[i]):
            cur_op = s[i]
            if may_be_unary and is_unary(cur_op):
                cur_op = 'u' + cur_op
            while op and (
                    (cur_op[0] != 'u' and priority(op[-1]) >= priority(cur_op)) or
                    (cur_op[0] == 'u' and priority(op[-1]) > priority(cur_op))
                ):
                process_op(st, op[-1])
                op.pop()
            op.append(cur_op)
            may_be_unary = True
        else:
            number = 0
            while i < len(s) and s[i].isalnum():
                number = number * 10 + ord(s[i]) - ord('0')
                i += 1
            i -= 1
            st.append(number)
            may_be_unary = False
        i += 1

    while op:
        process_op(st, op[-1])
        op.pop()
    return st[-1]
