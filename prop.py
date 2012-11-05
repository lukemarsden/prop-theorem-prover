#!/usr/bin/env python

# PropVar
# Connective


class PropVar(object):
    def __init__(self, value):
        self.value = value


    def evaluate(self):
        print "PV, my value is", self.value
        return self.value



class Not(object):
    def __init__(self, variable):
        self.variable = variable


    def evaluate(self):
        print "evaluating NOT"
        return not self.variable.evaluate()



class And(object):
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2


    def evaluate(self):
        print "evaluating AND"
        return self.v1.evaluate() and self.v2.evaluate()



p = PropVar(True)
q = PropVar(False)

# p ^ ~q
print And(p, Not(q)).evaluate()

"""
evaluating AND
PV, my value is True
evaluating NOT
PV, my value is False
True
"""


