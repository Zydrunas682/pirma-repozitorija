
# print("Aš esu funkcijoje")
# #iškvietimas:
# fn_namedef fn_name():




def check_speed(speed):
    if speed <= 50:
        return "Ok"
    else:
        penalty_points = (speed - 50) // 5
        if penalty_points >= 8:
            return f"{penalty_points} - Vairuotojo teisės atimamos"
        else:
            return penalty_points

# Įvedame greitį
user_input = input("Įveskite automobilio greitį (km/h): ")
try:
    speed = int(user_input)  # Paverčiame į sveikąjį skaičių
    result = check_speed(speed)  # Iškviečiame funkciją su vartotojo įvestu greičiu
    print(result)  # Išvedame rezultatą
except ValueError:
    print("Prašome įvesti galiojantį skaičių.")




# 


# Įvedame greitį
user_input = input("Įveskite automobilio greitį (km/h): ")
try:
    speed = int(user_input)  # Paverčiame į sveikąjį skaičių
    result = check_speed(speed)  # Iškviečiame funkciją su vartotojo įvestu greičiu
    print(result)  # Išvedame rezultatą
except ValueError:
    print("Prašome įvesti galiojantį skaičių.")




def check_speed(speed):
    if speed <= 50:
        return "Ok"
    else:
        # Apskaičiuojame baudos taškus
        penalty_points = (speed - 50) // 5
        
        # Tikriname, ar taškų suma yra 8 ar daugiau
        if penalty_points >= 8:
            return f"{penalty_points} - Vairuotojo teisės atimamos"
        else:
            return penalty_points

# Pavyzdžiai
print(check_speed(40))  # Išves: Ok
print(check_speed(70))  # Išves: 4
print(check_speed(90))  # Išves: 8 - Vairuotojo teisės atimamos
60



# Sukuriame du set'us
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
set3 = {4,7,8,2,4,9,5}

# Naudojame intersection() metodą
common_elements = set1.intersection(set2,set3)

print(common_elements)  # Išves: {4, 5}



a = 5
a += 3
print (a)





print (3+8)


