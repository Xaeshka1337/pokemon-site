import requests

name = input("Введите имя покемона: ")

url = f"https://pokeapi.co/api/v2/pokemon/{name}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n--- Информация о покемоне ---")
    print("Имя:", data["name"])
    print("ID:", data["id"])
    print("Рост:", data["height"])
    print("Вес:", data["weight"])

    print("Тип:", data["types"][0]["type"]["name"])

else:
    print("Покемон не найден")