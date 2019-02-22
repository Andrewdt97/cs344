from csp import  parse_neighbors, CSP, min_conflicts


def printResult( res ):
    for state in res:
        print( state + ": " + res[state] )


def schedule_constraint(varA, domA, varB, domB, recurse=0):
    if varA == varB and domA == domB:
        return False

    # Parse strings into arrays
    # [0] : Prof, [1] : Time, [2] : Room
    domAList = domA.split(',')
    domBList = domB.split(',')

    # Professor cannot teach two classes at the same time
    if domAList[0] == domBList[0] and domAList[1] == domBList[1]:
        return False

    # A room cannot be double occupied
    if domAList[2] == domBList[2] and domAList[1] == domBList[1]:
        return False

    # Specific constraints
    if varA == 'cs108' and domAList[0] != 'DS':
        return False

    if varA == 'cs112' and domAList[0] != 'JA':
        return False

    if recurse == 0:
        return schedule_constraint(varB, domB, varA, domA, 1)

    return True


profs = 'KVL, JA, DS, HP,'.split()
times = '800MWF, 900MWF, 1030MWF, 1130MWF, 830TT, 1030TT,'.split()
rooms = 'NH253 SB382'.split()
domainsList = []
# Create every permutation of professor, time, and room
for p in profs:
    for t in times:
        for r in rooms:
            key = p + t + r
            domainsList.append( key )

variables = ['cs108', 'cs112', 'cs104', 'cs212', 'cs214', 'cs262', 'cs232']
domains = {}
# Assign each class to all the domain permutations
for var in variables:
    domains[var] = domainsList
neighbors = parse_neighbors("""cs108: DS,800MWF,NH253""", variables)
for type in [domainsList, variables]:
    for A in type:
        for B in type:
            if A != B:
                if B not in neighbors[A]:
                    neighbors[A].append(B)
                if A not in neighbors[B]:
                    neighbors[B].append(A)

problem = CSP(variables, domains, neighbors, schedule_constraint)

result = min_conflicts(problem, max_steps=1000)

print("Min conflicts:")
printResult( result)