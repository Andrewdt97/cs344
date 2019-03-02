# Andrew Thomas
# CS344 Lab05
# 03/01/19

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.20}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.20})
    ])

# a. P(Cancer | positive results on both tests)
'''
Handwork:
P(C | T1 ^ T2) = alpha <P(T1 | C) * P(T2 | C) * P(C), P(T1 | -C) * P(T2 | -C) * P(-C))
    = alpha <0.9 * 0.9 * 0.01,  0.2 * 0.2 * 0.99>
    = alpha <0.0081, 0.0396>
    = <0.17, 0.83>
    This is a bit suprising, but with the chance of cancer so low, it makes sense that there could be a lot of
    false positives.
'''
print( enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# b. P(Cancer | a positive result on test 1, but a negative result on test 2)
'''
Handwork:
P(C | T1 ^ -T2) = alpha <P(T1 | C) * P(-T2 | C) * P(C), P(T1 | -C) * P(-T2 | -C) * P(-C)
    = alpha <0.9 * 0.1 * 0.01, 0.2 * (1 - 0.2) * 0.99)
    = alpha <0.0009, 0.1584>
    = <0.00565, 0.994>
    This makes sense because false positives are bountiful given the chances of cancer. If two tests disagree
    one was likely a false postive, putting the chances of cancer very low.
'''
print( enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())