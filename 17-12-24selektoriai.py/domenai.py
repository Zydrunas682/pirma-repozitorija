# import requests

# url = "https://www.thecocktaildb.com/browse/search/?s=margarita"

# response =requests.get(url)

# print(response.text)

import requests

# CocktailDB API URL, skirtas gėrimų paieškai pagal pavadinimą
url = "https://www.thecocktaildb.com/api/json/v1/1/search.php?s=margarita"

# At sending GET užklausą į API
response = requests.get(url)

# Spausdiname atsakymą JSON formatu
print(response.json())


import requests

# Prašome vartotojo įvesti kokteilio pavadinimą
cocktail_name = input("Įveskite kokteilio pavadinimą: ")

# Sukuriame API URL su vartotojo įvestu kokteilio pavadinimu
url = f"https://www.thecocktaildb.com/api/json/v1/1/search.php?s={cocktail_name}"

# Siunčiame GET užklausą į API
response = requests.get(url)

# Patikriname, ar gauta atsakymas
if response.status_code == 200:
    # Išvedame atsakymą JSON formatu
    data = response.json()
    if data["drinks"]:
        # Jeigu kokteilis rastas, atspausdiname pirmąją informaciją apie jį
        print(f"Kokteilio pavadinimas: {data['drinks'][0]['strDrink']}")
        print(f"Ingredientai ir kiekiai:")
        for i in range(1, 16):
            ingredient = data['drinks'][0].get(f"strIngredient{i}")
            measure = data['drinks'][0].get(f"strMeasure{i}")
            if ingredient:
                print(f"{ingredient}: {measure if measure else 'Nenurodyta'}")
        print(f"Instrukcija: {data['drinks'][0]['strInstructions']}")
    else:
        print("Kokteilis nerastas.")
else:
    print("Įvyko klaida bandant prisijungti prie API.")

