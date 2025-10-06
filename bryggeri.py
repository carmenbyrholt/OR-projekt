from pulp import *
problem = LpProblem('mængde i tankene', LpMinimize)

f01 = LpVariable('brændstofforbrug i havn 0 til 1 i tank 1', lowBound=0)
f02 = LpVariable('brændstofforbrug i havn 0 til 1 i tank 2', lowBound=0)
f11 = LpVariable('brændstofforbrug i havn 1 til 2 i tank 1', lowBound=0)
f12 = LpVariable('brændstofforbrug i havn 1 til 2 i tank 2', lowBound=0)
f21 = LpVariable('brændstofforbrug i havn 2 til 3 i tank 1', lowBound=0)
f22 = LpVariable('brændstofforbrug i havn 2 til 3 i tank 2', lowBound=0)
f31 = LpVariable('brændstofforbrug i havn 3 til 0 i tank 1', lowBound=0)
f32 = LpVariable('brændstofforbrug i havn 3 til 0 i tank 2', lowBound=0)

l01 = LpVariable('Mængden af brændstof fyldt i tank 1 ved havn 0', lowBound=0)
l02 = LpVariable('Mængden af brændstof fyldt i tank 2 ved havn 0', lowBound=0)
l11 = LpVariable('Mængden af brændstof fyldt i tank 1 ved havn 1', lowBound=0)
l12 = LpVariable('Mængden af brændstof fyldt i tank 2 ved havn 1', lowBound=0)
l21 = LpVariable('Mængden af brændstof fyldt i tank 1 ved havn 2', lowBound=0)
l22 = LpVariable('Mængden af brændstof fyldt i tank 2 ved havn 2', lowBound=0)
l31 = LpVariable('Mængden af brændstof fyldt i tank 1 ved havn 3', lowBound=0)
l32 = LpVariable('Mængden af brændstof fyldt i tank 2 ved havn 3', lowBound=0)

h01 = LpVariable('Mængden af brændstof i tank 1 ved afgang fra havn 0', lowBound=0)
h02 = LpVariable('Mængden af brændstof i tank 2 ved afgang fra havn 0', lowBound=0)
h11 = LpVariable('Mængden af brændstof i tank 1 ved afgang fra havn 1', lowBound=0)
h12 = LpVariable('Mængden af brændstof i tank 2 ved afgang fra havn 1', lowBound=0)
h21 = LpVariable('Mængden af brændstof i tank 1 ved afgang fra havn 2', lowBound=0)
h22 = LpVariable('Mængden af brændstof i tank 2 ved afgang fra havn 2', lowBound=0)
h31 = LpVariable('Mængden af brændstof i tank 1 ved afgang fra havn 3', lowBound=0)
h32 = LpVariable('Mængden af brændstof i tank 2 ved afgang fra havn 3', lowBound=0)

#Objective Function
problem += 600*(l01+l02)+900*(l11+l12)+1100*(l21+l22)+1200*(l31+l32), 'Objective Function'

#Constraints
problem += f01 <= h01, 'capacity constraint 1'
problem += f02 <= h02, 'capacity constraint 1'
problem += f11 <= h11, 'capacity constraint 1'
problem += f12 <= h12, 'capacity constraint 1'
problem += f21 <= h21, 'capacity constraint 1'
problem += f22 <= h22, 'capacity constraint 1'
problem += f31 <= h31, 'capacity constraint 1'
problem += f32 <= h32, 'capacity constraint 1'


problem +=  h11 = h01+l11-f01, 'capacity constraint 2'
problem +=  h12 = h02+l12-f02, 'capacity constraint 2'
problem +=  h21 = h11+l21-f11, 'capacity constraint 2'
problem +=  h22 = h12+l22-f12, 'capacity constraint 2'
problem +=  h31 = h21+l31-f21, 'capacity constraint 2'
problem +=  h32 = h22+l32-f22, 'capacity constraint 2'

problem +=  h01 = h31+l01-f31, 'capacity constraint 3'
problem +=  h02 = h32+l02-f32, 'capacity constraint 3'

problem +=  f01+f02 = F0, 'capacity constraint 6'
problem +=  f11+f12 = F1, 'capacity constraint 6'
problem +=  f21+f22 = F2, 'capacity constraint 6'
problem +=  f31+f32 = F3, 'capacity constraint 6'

R0=1000
R1>=1200
R2>=1800
R3>=2800

problem +=  h01+h02 => R1+F0, 'capacity constraint 4'
problem +=  h11+h12 => R2+F1, 'capacity constraint 4'
problem +=  h21+h22 => R3+F2, 'capacity constraint 4'

problem +=  h31+h32 => R0+F3, 'capacity constraint 5'

print("omkostning: ", value(problem.objective))
