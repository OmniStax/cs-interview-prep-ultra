import sys

MOD = 10 ** 9 + 7


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    # one running value per open bracket; at an even depth it is a sum, at an odd depth a product
    stack = [0]
    for t in data[1:1 + n]:
        if t == '(':
            stack.append(1 if len(stack) % 2 == 1 else 0)
        else:
            v = stack.pop() if t == ')' else int(t)
            if len(stack) % 2 == 0:
                stack[-1] = stack[-1] * v % MOD
            else:
                stack[-1] = (stack[-1] + v) % MOD
    print(stack[0])


main()
