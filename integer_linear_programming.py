from pulp import *
import time

start_time = time.time()
K = 1 #the number of sales people 
sites = ["Takkali-1", "Takkali-29", "Emek-4", "Şarhöyük"]
distances = {("Takkali-1", "Takkali-29"): 2.8,
             ("Takkali-1", "Emek-4"): 3.9,
             ("Takkali-1", "Şarhöyük"): 1.5,
             ("Takkali-29", "Takkali-1"):  2.8,
             ("Takkali-29", "Emek-4"): 0.8,
             ("Takkali-29", "Şarhöyük"): 4.0,
             ("Emek-4", "Takkali-1"): 3.9,
             ("Emek-4", "Takkali-29"): 0.8,
             ("Emek-4", "Şarhöyük"): 4.1,
             ("Şarhöyük", "Takkali-1"): 1.5,
             ("Şarhöyük", "Takkali-29"): 4.0,
             ("Şarhöyük", "Emek-4"): 4.1}

prob=LpProblem("vehicle", LpMinimize)
#indicator variable if site i is connected to site j in the tour
x = LpVariable.dicts('x',distances, 0,1,LpBinary)
#dummy vars to eliminate subtours
u = LpVariable.dicts('u', sites, 0, len(sites)-1, LpInteger)
#the objective
cost = lpSum([x[(i,j)]*distances[(i,j)] for (i,j) in distances])
prob+=cost
#constraints
for k in sites:
    cap = 1 if k != "Takkali-29" else K
    #inbound connection
    prob+= lpSum([ x[(i,k)] for i in sites if (i,k) in x]) ==cap
    #outbound connection
    prob+=lpSum([ x[(k,i)] for i in sites if (k,i) in x]) ==cap
    
#subtour elimination
N=len(sites)/K
for i in sites:
    for j in sites:
        if i != j and (i != "Takkali-29" and j!= "Takkali-29") and (i,j) in x:
            prob += u[i] - u[j] <= (N)*(1-x[(i,j)]) - 1

prob.solve()
for variable in prob.variables():
    print(f"{variable.name}: {variable.varValue}")
import matplotlib.pyplot as plt

plt.hist()

# Display the map
plt.show()
# print('Longest time spent:', totalTime, '(min)')
print('Total Distance for Integer Linear Programming:', value(prob.objective), 'km')
print(f"Algorithm Time: {time.time() - start_time}")