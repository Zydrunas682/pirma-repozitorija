

s = set() # sukuriamas tuščias rinkinys
print(s)
s = set(['M','A', 'B', 'C']) #iš sąrašo
print(s)
s = {'B', 'A', 'C', 'M'} #tiesiogiai
print(s)


s = set() # sukuriamas tuščias rinkinys
print(s)



s = set(['M', 'A', 'B', 'C'])  # iš sąrašo
print(s)  # Išves: {'A', 'B', 'C', 'M'}


s = set(['a','b','c',' d','b'])
print (s)


s =set (['B', 'A', 'C', 'M'])  # tiesiogiai
print(s)  # Išves: {'A', 'B', 'C', 'M'}



# Rinkiniai
s1 = {'A', 'B', 'C'}
s2 = {'B', 'C', 'D'}

# Sąjunga
s3 = s1 | s2
print("Sąjunga:", s3)  # Išves: {'A', 'B', 'C', 'D'}

# Persidengimas set
s4 = s1 & s2
print("Persidengimas:", s4)  # Išves: {'B', 'C'}

# Skirtumas
s5 = s1 - s2
print("Skirtumas:", s5)  # Išves: {'A'}


a_set = {1, 2, 3, 4, 'a'}
b_set = {1, 2, 3, 5, 6, 'b'}

print("a_set:", a_set)  # Išves: a_set: {1, 2, 3, 4, 'a'}
print("b_set:", b_set)  # Išves: b_set: {1, 2, 3, 5, 6, 'b'}


a_set = {1,2,3,4,'a'}
b_set = {1,2,3,4,5,'c'}

print('a set;', a_set)
print('b set;', b_set)



a_set = {1, 2, 3, 4, 'a'}
b_set = {1, 2, 3, 5, 6, 'b'}

# Rasti sąjungą
sąjunga = a_set | b_set

# Išvesti rezultatą
print("Sąjunga:", sąjunga)



# a_set = {1, 2, 3, 4, 'a'}
# b_set = {1, 2, 3, 5, 6, 'b'}

# # Rasti bendrus elementus
# bendri_elementai = a_set & b_set

# # Išvesti rezultatą
# print("Bendri elementai:", bendri_elementai)



a_set = {1, 2, 3, 4, 'a'}
b_set = {1, 2, 3, 5, 6, 'b'}

# Rasti bendrus elementus
bendri_elementai = a_set & b_set

# Išvesti rezultatą
print("Bendri elementai:", bendri_elementai)



# Žodynai su informacija apie prekes
d1 = {"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200}
d2 = {"cost_price": 225.89, "sell_price": 550.00, "inventory": 100}
d3 = {"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500}

# Funkcija pelnui apskaičiuoti
def calculate_profit(product):
    cost_price = product["cost_price"]
    sell_price = product["sell_price"]
    inventory = product["inventory"]
    
    profit_per_item = sell_price - cost_price
    total_profit = profit_per_item * inventory
    
    return total_profit

# Apskaičiuoti bendrą pelną
total_profit = calculate_profit(d1) + calculate_profit(d2) + calculate_profit(d3)

# Išvesti rezultatą
print(f"Bendras pelnas: {total_profit:.2f}")

