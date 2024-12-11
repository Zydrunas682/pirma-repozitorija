numbers = [str(i) for i in range(1, 3001) if i % 77 == 0]
result = ",".join(numbers)
print(result)






# Prašome vartotojo įvesti simbolį ir kraštinės ilgį
symbol = input("Įveskite simbolį: ")
size = int(input("Įveskite kvadrato kraštinės ilgį: "))

# Nupieškime tuščiavidurį kvadratą
for i in range(size):
    if i == 0 or i == size - 1:  # Pirmas ir paskutinis eilučių atspausdinimas
        print(symbol * size)
    else:  # Vidurinės eilutės
        print(symbol + ' ' * (size - 2) + symbol)




# Prašome vartotojo įvesti simbolį ir kvadrato kraštinės ilgį
symbol = input("Įveskite simbolį: ")
size = int(input("Įveskite kvadrato kraštinės ilgį: "))

# Nupieškime kvadratą
for i in range(size):
    print((symbol + '') * size)





#     # Prašome vartotojo įvesti simbolį ir kvadrato kraštinės ilgį
# symbol = input("Įveskite simbolį: ")
# size = int(input("Įveskite kvadrato kraštinės ilgį (ne mažiau kaip 3): "))

# # Nupieškime kvadratą su įstriža žvaigždute
# for i in range(size):
#     for j in range(size):
#         if i == j or j == size - i - 1:  # Įstrižainės
#             print(symbol, end=' ')
#         else:
#             print('*', end=' ')  # Pagrindinis simbolis
#     print()  # Naujai eil




# Symbol = input("iveskite simboli: ")
# dydis = int(input("iveskite kvadrato krastines ilgi(nemaziau kaip 3): "))

# for i in range(dydis):
#     for j in range(dydis):
#         if i == j or j == dydis - i - 1:
#             print(symbol  , end='')
#         else:
#             print(' * ',end='')
#     print()
            

# if i == j:
# or j == dydis - i - 1




A = float(input("Įveskite skaičių A: "))
B = float(input("Įveskite skaičių B: "))

# Prašome vartotojo pasirinkti matematinį veiksmą
veiksmas = input("Pasirinkite veiksmą (+, 5
                 −, /, *): ")

try:
    if veiksmas == '+':
        rezultatas = A + B
    elif veiksmas == '-':
        rezultatas = A - B
    elif veiksmas == '*':
        rezultatas = A * B
    elif veiksmas == '/':
        if B == 0:
            raise ValueError("Dalyba iš 0 yra negalima.")  # Keliame klaidą, jei B yra 0
        rezultatas = A / B
    else:
        print("Neteisingas veiksmas. Pasirinkite vieną iš: +, −, /, *")
        exit()  # Išeiname, jei veiksmas neteisingas

    print(f"Rezultatas: {rezultatas}")

except ValueError as e:
    print("Klaida:", e)




name = "Jonas"
age = 30
message = f"Mano vardas yra {name}, o man yra {age} metų."
print(message)
