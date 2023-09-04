import math

n0 = 100
halfingTime = 5730

S = float(input('Input the amount of years: '))

y = math.log(2) / halfingTime
n = n0 * math.exp(-y * S)

print(f'The remaining % after {S} years is {n:.2f}% of the 14C isotope')
