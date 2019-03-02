# Andrew Thomas
# CS344 Lab05
# 03/01/19

from probability import BayesNet, enumeration_ask

# Utility variables
T, F = True, False

happiness = BayesNet([
    ('Sunny', '', 0.70),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.70, (F, T): 0.9, (F, F): 0.01})
    ])

# a.
# i. P(Raise | sunny)
'''
Handwork:
The status of a raise is independant of the sun, so the probability is the given 0.01
'''
print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())

# ii. P(Raise | happy ∧ sunny)
'''
Handwork:
P(R | h ^ s) = alpha <P(h | R ^ s) * P(R) * P(s), P(h | -R ^ s) * P(-R) * P(s)> 
    = alpha <1 * 0.01 * 0.70, 0.7 * 0.99 * 0.7>
    = alpha <0.007, .4851>
    = <.0142, 0.986>
'''
print(enumeration_ask('Raise', dict(Sunny=T, Happy=T), happiness).show_approx())

# b.
# i. P(Raise | happy)
'''We know that if he gets a raise, he is most certainly happy, therefore the chance of raise is almost
    that of the raise independant of happiness.'''
print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())

# ii. P(Raise | happy ∧ ¬sunny)
''' If it's not sunny, it is almost certain that he is unhappy. Since he is happy, we have decent reason to believe
    he got a raise. However, since the chance of the raise was so low, it remains a modest probability.'''
print( enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())
