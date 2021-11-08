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