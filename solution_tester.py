
from math import sqrt as sqrt
from re import T
from sympy import E, symbols, Eq, solve

tested_solution_dictionary = []

br_values = [63.56/100, 5.07/100, 3.352/100, 20.67/100, 1.76/100, 5.583/100, 6.2/1000, 4/1000, 3.3/1000, 3/1000]

a, b, c, d, e, f, g, h, i, j = symbols("a, b, c, d, e, f, g, h, i, j")

velocity = int(input("Please enter the velocity value: "))
electron_n = int(input("Please enter the electron number: "))
kplus_n = int(input("Please enter the Kaon+ number: "))
piplus_n = int(input("Please enter the π+ number: "))
pinegative_n = int(input("Please enter the π- number: "))

gamma = (1/sqrt(1 - velocity**2 / 299792458**2))

sol1 = ((gamma) * (1.238*10**8))
eq1 = Eq((a*(br_values[0]) + b*(br_values[1]) + c*(br_values[2]) + d*(br_values[3]) + e*(br_values[4]) + f*(br_values[5]) + g*(br_values[6]) + h*(br_values[7]) + i*(br_values[8]) + j*(br_values[9]) ), sol1)


for i in br_values:
  eq_library = []
  eq_library.append(eq1)


solution_dictionary = solve((eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0], eq_library[0]), (a, b, c, d, e, f, g, h, i, j))

# Electron number test
eq1 = Eq((kplus_n * (solution_dictionary[1] * solution_dictionary[9])), electron_n)
if(solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[1], solution_dictionary[9])

# π+ number test
eq1 = Eq((kplus_n * (solution_dictionary[3] + solution_dictionary[4] + 2*solution_dictionary[5])) , piplus_n)
if(solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[3], solution_dictionary[4], solution_dictionary[5])

# π- number test
eq1 = Eq((kplus_n * (solution_dictionary[5])), pinegative_n)
if (solve(eq1)):
  tested_solution_dictionary.append(solution_dictionary[5])