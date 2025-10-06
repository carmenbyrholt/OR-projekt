from pulp import *
problem = LpProblem('omkostninger', LpMinimize)
x1 = LpVariable('Mombasa', lowBound=0)
x2 = LpVariable('Zanzibar', lowBound=0)
x3 = LpVariable('Victoria', lowBound=0)
x4 = LpVariable('Salaha', lowBound=0)
#Objective Function
problem += 600*x1+900*x2+1100*x3+1200*x4 , 'Objective Function'
#Constraints
problem += 3*x1 + 2*x2 <= 5, 'capacity constraint 1'
problem +=   x1 + 4*x2 <= 8, 'capacity constraint 2'
problem +=   x1 + 4*x2 <= 8, 'capacity constraint 3'
problem +=   x1 + 4*x2 <= 8, 'capacity constraint 4'

print("Current Status: ", LpStatus[problem.status])
problem.solve()
print("Mængde af øl1: ", x1.varValue)
print("Mængde af øl2: ", x2.varValue)
print("Profit: ", value(problem.objective))


from pulp import *
problem = LpProblem('Bryggeri_optimering', LpMaximize)
x1 = LpVariable('beer1', lowBound=0)
x2 = LpVariable('beer2', lowBound=0)
#Objective Function
problem += 4*x1 + 5*x2 , 'Objective Function'
#Constraints
problem += 3*x1 + 2*x2 <= 5, 'capacity constraint 1'
problem +=   x1 + 4*x2 <= 8, 'capacity constraint 2'
print("Current Status: ", LpStatus[problem.status])
problem.solve()
print("Mængde af øl1: ", x1.varValue)
print("Mængde af øl2: ", x2.varValue)
print("Profit: ", value(problem.objective))