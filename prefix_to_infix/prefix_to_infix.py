class PrefixToInfixConverter:
    def __init__(self):
        self.operators = set(['+', '-', '*', '/'])

    def is_operator(self, token):
        return token in self.operators

    def prefix_to_infix(self, expression):
        stack = []
        tokens = expression.split()

        try:
            for token in reversed(tokens):
                if self.is_operator(token):
                    if token in {'+', '-'} and len(stack) == 1:
                        operand = stack.pop()
                        stack.append(f"({token}{operand})")
                    else:
                        operand1 = stack.pop()
                        operand2 = stack.pop()
                        stack.append(f"({operand1} {token} {operand2})")
                else:
                    stack.append(token)

            if len(stack) != 1:
                raise ValueError("Invalid expression")

            return stack[0]
        except IndexError:
            raise ValueError("Invalid expression")
