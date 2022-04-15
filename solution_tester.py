
from math import sqrt as sqrt
from re import T
from sympy import E, symbols, Eq, solve

tested_solution_dictionary = []

br_values = [63.56/100, 5.07/100, 3.352/100, 20.67/100, 1.76/100, 5.583/100, 6.2/1000, 4/1000, 3.3/1000, 3/1000]

a, b, c, d, e, f, g, h, i, j = symbols("a, b, c, d, e, f, g, h, i, j")

velocity = int(input("Please enter the velocity value: "))
positron_n = int(input("Please enter the electron number: "))
kplus_n = int(input("Please enter the Kaon+ number: "))
piplus_n = int(input("Please enter the π+ number: "))
pinegative_n = int(input("Please enter the π- number: "))
muon_n = int(input("Please enter the muon number: "))

gamma = (sqrt(1 - velocity**2 / 299792458**2))

sol1 = ((gamma) * (1.238*10**8))
eq1 = Eq((a*7.869*10**7 + b*6.277*10**6 + c*4.129*10**6 + d*2.559*10**7 + e*2.179*10**6 + f*2.179*10**6), sol1)


for i in br_values:
  eq_library = []
  eq_library.append(eq1)


solution_dictionary = solve((eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0]), (a, b, c, d, e, f, g, h, i, j))

# Positron number test
eq1 = Eq((kplus_n * (solution_dictionary[1]*0.0507 * solution_dictionary[9])*0.003), positron_n)
if(solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[1], solution_dictionary[9])
  
# Muon number test
eq1 = Eq((kplus_n *(solution_dictionary[0]*0.6349 + solution_dictionary[2]*0.3333 + solution_dictionary[6]*0.0062) + solution_dictionary[7]*0.004 + solution_dictionary[8]*0.0033), muon_n)
if(solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[0], solution_dictionary[2], solution_dictionary[6], solution_dictionary[7], solution_dictionary[8])

# π+ number test
eq1 = Eq((kplus_n * (solution_dictionary[3]*0.2067 + solution_dictionary[4]*0.0176 + 2*solution_dictionary[5])*0.0558) , piplus_n)
if(solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[3], solution_dictionary[4], solution_dictionary[5])

# π- number test
eq1 = Eq((kplus_n * (solution_dictionary[5])*0.0558), pinegative_n)
if (solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[5])
