import webhandler
import re

def match_query(regex, query):
    return len(re.findall(regex, query)) > 0

class QuerySolver(object):
    def __init__(self):
        pass

    def answer_query(self, query):
        """Answer a query"""
        if match_query(r'^\d+ \d+ [\*\+]$', query):
            return self._rpn1(query)

        return 85
    
    def evalEx(self,query):
        precedence = {"+":1,"-":1,"*":2,"/":2}
        integerStack = []
        operatorStack = []
        for i in range(len(query.split())):
            if query.split()[i] == "(":
                operatorStack.append("(")
            elif re.findall("[0-9]",query.split()[i]):
                number = 0
                while (i < len(query.split()) and
                query.split()[i].isdigit()):
                    number = 10*
             
                val = (val * 10) + int([i])
                i += 1
        
    def _rpn1(self, query):
        m = re.match(r'^(\d+) (\d+) ([\*\+])$', query)
        groups = m.groups()
        n1 = int(groups[0])
        n2 = int(groups[1])
        op = groups[2]

        if op == '+':
            return n1 + n2
        else:
            return n1 * n2