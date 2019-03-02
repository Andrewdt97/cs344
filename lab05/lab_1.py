'''
This module implements the Bayesian network shown in the text, Figure 14.2.
It's taken from the AIMA Python code.

@author: kvlinden
@version Jan 2, 2013
@author: adt8
@date: 03/01/19
'''

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
burglary = BayesNet([
    ('Burglary', '', 0.001),
    ('Earthquake', '', 0.002),
    ('Alarm', 'Burglary Earthquake', {(T, T): 0.95, (T, F): 0.94, (F, T): 0.29, (F, F): 0.001}),
    ('JohnCalls', 'Alarm', {T: 0.90, F: 0.05}),
    ('MaryCalls', 'Alarm', {T: 0.70, F: 0.01})
    ])

# i. P(Alarm | burglary ∧ ¬earthquake)
'''This is given in the network definition'''
print(enumeration_ask('Alarm', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# ii. P(John | burglary ∧ ¬earthquake)
'''John wil almost certainly call if there is an alarm, and the alarm will almost certainly fire when there is
    a breakin, so it makes sense that the result is close to 1, while not exceeding either of the conditional
    probabilities.'''
print(enumeration_ask('JohnCalls', dict(Burglary=T, Earthquake=F), burglary).show_approx())

# iii. P(Burglary | alarm)
'''The chance of an alarm from an earthquake is decently high. Therefore it makes sense that an alarm only gives
    a moderate chance of there being a burglary.'''
print(enumeration_ask('Burglary', dict(Alarm=T), burglary).show_approx())

# iv. P(Burglary | john ∧ mary)
'''This is related to the above, only a little bit less of a chance because John and Mary do not always call.'''
print(enumeration_ask('Burglary', dict(JohnCalls=T, MaryCalls=T), burglary).show_approx())
