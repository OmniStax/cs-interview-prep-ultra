import sys


def priority(op):
    if op[0] == 'u':
        return 3
    if op in '+-':
        return 1
    return 2


def process_op(st, op):
    if op[0] == 'u':
        l = st.pop()
        st.append(-l if op == 'u-' else l)
    else:
        r = st.pop()
        l = st.pop()
        if op == '+':
            st.append(l + r)
        elif op == '-':
            st.append(l - r)
        elif op == '*':
            st.append(l * r)
        else:
            st.append(l / r)


def evaluate(s):
    # two stacks, as cp-algorithms evaluates an expression: numbers on st, operators and brackets on op
    st, op = [], []
    may_be_unary = True
    i = 0
    while i < len(s):
        c = s[i]
        if c.isspace():
            i += 1
            continue
        if c == '(':
            op.append('(')
            may_be_unary = True
        elif c == ')':
            while op[-1] != '(':
                process_op(st, op.pop())
            op.pop()
            may_be_unary = False
        elif c in '+-*/':
            cur = 'u' + c if may_be_unary and c in '+-' else c
            while op and op[-1] != '(' and (priority(op[-1]) > priority(cur) if cur[0] == 'u'
                                            else priority(op[-1]) >= priority(cur)):
                process_op(st, op.pop())
            op.append(cur)
            may_be_unary = True
        else:
            j = i
            while j < len(s) and s[j].isdigit():
                j += 1
            st.append(int(s[i:j]))
            i = j - 1
            may_be_unary = False
        i += 1
    while op:
        process_op(st, op.pop())
    return st[-1]


for line in sys.stdin:
    if line.strip():
        out = f"{evaluate(line):.2f}"
        print("0.00" if out == "-0.00" else out)
