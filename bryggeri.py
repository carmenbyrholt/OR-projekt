from pulp import *
problem = LpProblem('mængde i tankene', LpMinimize)

f01 = LpVariable('brændstofforbrug i havn 0 til 1 i tank 1', lowBound=0)
f02 = LpVariable('brændstofforbrug i havn 0 til 1 i tank 2', lowBound=0)
f11 = LpVariable('brændstofforbrug i havn 1 til 2 i tank 1', lowBound=0)
f12 = LpVariable('brændstofforbrug i havn 1 til 2 i tank 2', lowBound=0)
f21 = LpVariable('brændstofforbrug i havn 2 til 3 i tank 1', lowBound=0)
f22 = LpVariable('brændstofforbrug i havn 2 til 3 i tank 2', lowBound=0)
f31 = LpVariable('brændstofforbrug i havn 3 til 4 i tank 1', lowBound=0)
f32 = LpVariable('brændstofforbrug i havn 3 til 3 i tank 2', lowBound=0)

l01 = LpVariable('', lowBound=0)
l02 = LpVariable('tank_2', lowBound=0)
l11 = LpVariable('', lowBound=0)
l12 = LpVariable('tank_2', lowBound=0)
l21 = LpVariable('', lowBound=0)
l22 = LpVariable('tank_2', lowBound=0)
l31 = LpVariable('', lowBound=0)
l32 = LpVariable('tank_2', lowBound=0)

h01 = LpVariable('', lowBound=0)
h02 = LpVariable('tank_2', lowBound=0)
h11 = LpVariable('', lowBound=0)
h12 = LpVariable('tank_2', lowBound=0)
h21 = LpVariable('', lowBound=0)
h22 = LpVariable('tank_2', lowBound=0)
h31 = LpVariable('', lowBound=0)
h32 = LpVariable('tank_2', lowBound=0)

#Objective Function
problem += 600*x1+900*x2+1100*x3+1200*x4 , 'Objective Function'
#Constraints

s = [1,2] #tank 
i =[0,1,2,3] #havne

# f_is er Mængden af brændstofforbrug fra tank s paa rejsen fra havn i til havn i + 1
f_is = {0: 700, 1: 1800, 2: 2200, 3: 2800} #forbrug

#l_is er Mængden af brændstof fyldt i tank s ved havn i
def l_is(i):
  if i==0:
    return 4000
  elif i==1:
    return 2000
  elif i==2:
    return 1500
  elif i==3:
    return 0

#h_is er Mængden af brændstof i tank s ved afgang fra havn i
def h_is(i)):
  if i==0:
    return l_is(0)+1000
  if i==1:
    return l_is(1)+1200
  if i==2:
    return l_is(2)+1800
  if i==3 :
    return l_is(3)+2800

#R(i) Mængden af brændstof, som skal være i reserve, ved ankomst til havn i.
def R(i):
  if i==0:
    return 5000
  elif i==1:
    return 1200
  elif i==2:
    return 1800
  elif i==3:
    return 2800
  
#F(i) Mængden af brændstof, som der er behov for, ved en sejlads fra havn i til havn i+1


def F(i):
  if f_is+R(i)


problem += f_is <= h_is(i), 'capacity constraint 1'
problem +=  h_is(i) = h_is(i-1)+l_is(i)-(f_is-1), 'capacity constraint 2'
problem +=  h_is(0) = h_is(3)+l_is(0)-(f_is==3) , 'capacity constraint 3'
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
