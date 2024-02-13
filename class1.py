def is_number(token): # checks if a token is a number
    try:
        float(token)
        return True
    except ValueError:
        return False


def shunting_yard(expression):
    output_stack = [] # output liste : conventionally named output_stack 
    operator_stack = [] # a list storing operators 
    tokens = expression.split() # tokenizes the expression

    operators = {'+': 1, '-': 1, '*': 2, '/': 2} # dictionary of operators with their precedence 
    for token in tokens: # for loop that iterate through tokens 
        if is_number(token): # number check call
            output_stack.append(token) # if a token is a number token is appended to the output_stack
        elif token in operators: # if a token is in the operator dictionnary 

''' 

    as long as operator_stack is not empty and the last item in the operator_stack is an operator 
    and if the precedence of the last operator in the stack is higher then the currently pointed operator

    move the operator to the outpu_stack
    
'''
            while operator_stack and operator_stack[-1] in operators and operators[operator_stack[-1]] >= operators[token]:
                output_stack.append(operator_stack.pop())
            operator_stack.append(token) # continue
        elif token == '(': 
            operator_stack.append(token)
        elif token == ')':
            while operator_stack and operator_stack[-1] != '(': # handling the closing parenthesis
                output_stack.append(operator_stack.pop())
            operator_stack.pop()  

    while operator_stack: 
        output_stack.append(operator_stack.pop()) # continues

    return output_stack # return the final list


def evaluate(expression):
    output_stack = []
    operators = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y} # calculator's functions

    postfix_expression = shunting_yard(expression) # generate postfix notation
    for token in postfix_expression: # iterate through each token in the postfix notation
        if is_number(token):
            output_stack.append(float(token)) # checks if the token is a number
        elif token in operators: 
            if len(output_stack) < 2: # if less than 2 elements are in the output stack we raise error
                raise ValueError("Insufficient values in operation")
            operand2 = output_stack.pop() # we pop the second operator (as its a stack) to a variable
            operand1 = output_stack.pop() # same for second 
            result = operators[token](operand1, operand2) # we calculate results 
            output_stack.append(result) # output

    if len(output_stack) != 1:
        raise ValueError("Invalid expression") # handles cases where the expression isnt written in the entended format e.g. -20 20
    return output_stack.pop() # pops out the output and returns it


try: # self explanitory
    expr = input("Enter an expression: ")
    print(evaluate(expr))
except Exception as e:
    print(f"Error: {e}")
