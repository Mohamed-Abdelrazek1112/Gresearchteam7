import webhandler
import re

class RpnEvaluator(object):
    def __init__(self):
        pass

    def evaluate_rpn(self, rpn):
        """Evaluate RPN"""

        tokens = rpn.split()
        stack = []
        for token in tokens:
            if token.isdecimal():
                stack.append(int(token))
            elif token == '+':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 + n2)
            elif token == '*':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 * n2)
            elif token == '-':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 - n2)
            elif token == '/':
                n2 = stack.pop()
                n1 = stack.pop()
                stack.append(n1 // n2)

        return stack.pop()
        