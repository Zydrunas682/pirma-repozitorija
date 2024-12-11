import random

# Generuojame 300 atsitiktinių skaičių
skaičiai = [random.randint(0, 300) for _ in range(300)]

# Skaičiuojame, kiek skaičių yra didesnių už 150
dideli_skaičiai_count = sum(1 for sk in skaičiai if sk > 150)

# Atspausdiname skaičius, didesnius nei 275, skliausteliuose
rezultatas = ' '.join([f"[{sk}]" if sk > 275 else str(sk) for sk in skaičiai])

# Išvedame rezultatus
print(rezultatas)
print(f"Skaičių, didesnių už 150: {dideli_skaičiai_count}")


Kiekis = 10
Simbolis = "*"


for i in range(Kiekis):
    if i == 0 or i == Kiekis - 1:
        print(f"{Simbolis} " * Kiekis)
    else:
        print(f"{Simbolis} " + " " * ((Kiekis - 2)*2) + f"{Simbolis} ")



        # Prašome vartotojo įvesti simbolį ir kvadrato kraštinės ilgį
symbol = input("Įveskite simbolį: ")
size = int(input("Įveskite kvadrato kraštinės ilgį: "))

# Nupieškime kvadratą
for i in range(size):
    print((symbol + ' ') * size)raise