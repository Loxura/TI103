def is_number(token):
    try:
        float(token)
        return True
    except ValueError:
        return False


def shunting_yard(expression):
    output_stack = []
    operator_stack = []
    tokens = expression.split()

    operators = {'+': 1, '-': 1, '*': 2, '/': 2}
    for token in tokens:
        if is_number(token):
            output_stack.append(token)
        elif token in operators:
            while operator_stack and operator_stack[-1] in operators and operators[operator_stack[-1]] >= operators[token]:
                output_stack.append(operator_stack.pop())
            operator_stack.append(token)
        elif token == '(':
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(':
                output_stack.append(operator_stack.pop())
            operator_stack.pop()  # Remove the '(' from the stack

    while operator_stack:
        output_stack.append(operator_stack.pop())

    return output_stack


def evaluate(expression):
    output_stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y}

    postfix_expression = shunting_yard(expression)
    for token in postfix_expression:
        if is_number(token):
            output_stack.append(float(token))
        elif token in operators:
            if len(output_stack) < 2:
                raise ValueError("Insufficient values in operation")
            operand2 = output_stack.pop()
            operand1 = output_stack.pop()
            result = operators[token](operand1, operand2)
            output_stack.append(result)

    if len(output_stack) != 1:
        raise ValueError("Invalid expression")
    return output_stack.pop()


try:
    expr = input("Enter an expression: ")
    print(evaluate(expr))
except Exception as e:
    print(f"Error: {e}")
