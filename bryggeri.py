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

#constants
F0=700
F1=1800
F2=2200
F3=2800

R0=1000
R1=1200
R2=1800
R3=2800

#Constraints
problem += h01 <=3500
problem += h02 <=3500
problem += h11 <=3500
problem += h12 <=3500
problem += h21 <=3500
problem += h22 <=3500
problem += h31 <=3500
problem += h32 <=3500

problem += f01 <= h01
problem += f02 <= h02
problem += f11 <= h11
problem += f12 <= h12
problem += f21 <= h21
problem += f22 <= h22
problem += f31 <= h31
problem += f32 <= h32

problem +=  h01 == h31+l01-f31
problem +=  h02 == h32+l02-f32
problem +=  h11 == h01+l11-f01
problem +=  h12 == h02+l12-f02
problem +=  h21 == h11+l21-f11
problem +=  h22 == h12+l22-f12
problem +=  h31 == h21+l31-f21
problem +=  h32 == h22+l32-f22


problem +=  f01+f02 == F0
problem +=  f11+f12 == F1
problem +=  f21+f22 == F2
problem +=  f31+f32 == F3

problem +=  h01+h02 >= R1+F0
problem +=  h11+h12 >= R2+F1
problem +=  h21+h22 >= R3+F2
problem +=  h31+h32 >= R0+F3


problem.solve()
print("Status:", LpStatus[problem.status])
print("Omkostning:", value(problem.objective))
print(value(f01),value(f02),value(f11),value(f12),value(f21),value(f22),value(f31),value(f32))
#brændstofforbrug i havn i til havn i+1 i tank s
print(value(l01),value(l02),value(l11),value(l12),value(l21),value(l22),value(l31),value(l32))
#Mængden af brændstof fyldt i tank s ved havn i
print(value(h01),value(h02),value(h11),value(h12),value(h21),value(h22),value(h31),value(h32))
#Mængden af brændstof i tank s ved afgang fra havn i
