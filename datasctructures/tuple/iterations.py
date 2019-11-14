## Iterações

# Percorrer uma sequência de forma ordenada, utitlize sorted()
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']

for f in sorted(set(basket)):
    pass #print(f)

import math

#Não altere a sequência, crie uma nova com os valores desejados
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]

filtered_data = []

for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)