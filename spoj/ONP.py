from string import lowercase


def rpn(expr):
    def is_operator(e):
        return e in ('+', '-', '*', '/', '^')

    def is_operand(e):
        return e in lowercase
    
    def precedence(e):
        map = {'+': 0,
               '-': 0,
               '*': 1,
               '/': 1,
               '^': 2}
        return map[e]

    stack = []
    result = ''

    for e in expr:
        if is_operand(e):
            result += e
        elif is_operator(e):
            while stack and is_operator(stack[-1]) and precedence(stack[-1]) > precedence(e):
                result += stack.pop()
            stack.append(e)
        elif e == '(':
            stack.append(e)
        elif e == ')':
            while stack[-1] != '(':
                result += stack.pop()
            stack.pop()
    while stack:
        result += stack.pop()
    return result

N = int(raw_input())
for _ in xrange(N):
    expression = raw_input()
    print(rpn(expression))
