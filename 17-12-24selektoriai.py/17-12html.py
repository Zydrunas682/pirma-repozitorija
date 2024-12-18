# import requests
# from bs4 import BeautifulSoup

# def scrape_data():

#     base_url = ("https://sutarta.lt/skelbimai/garso-vaizdo-foto-technika/vaizdo-video-technika?")
#     ads = []
#     page = 1

#     while True:
#         url = f"{ base_url }?page_nr={page}"
#         response = requests. get(url)

#         soup = BeautifulSoup(response.text, "html.parser")
#         print(soup)
#         ad_elements = soup.select('li[id^="an_"]')

#         # Jei nėra skelbimų, nutraukiame ciklą
#         if not ad_elements:
#             print("Nebėra daugiau skelbimų, baigiame.")
#             break

#         # Ištraukiame duomenis apie kiekvieną skelbimą
#         for ad in ad_elements:
#             title = ad.get_text(strip=True)  # Pavadinimas
#             link = ad.find('a')['href'] if ad.find('a') else None  # Nuoroda, jei ji yra
#             ads.append({"title": title, "link": link})

#         # Pereiname prie kito puslapio
#         page += 1

#     return ads  # Grąžiname surinktus skelbimus

# # Naudojimas
# ads = scrape_data()
# print(ads)  # Išvedame surinktus skelbimus


import requests
name = input("iveskite norima kokteili")
url = f"www.thecocktaildb.com/api/json/v1/1/search.php?s={name}"

response = requests.get(url)
data = response.json()
for drink in data["drink"]:
  