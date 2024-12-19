import requests
import json

# Получение данных о странах
url = "https://restcountries.com/v3.1/subregion/Western%20Africa"
response = requests.get(url)
countries = response.json()

# Фильтрация стран с населением более 10 миллионов
filtered_countries = [
    {
        "name": country["name"]["common"],
        "capital": country.get("capital", ["N/A"])[0],
        "area": country.get("area", 0),
        "population": country.get("population", 0),
        "borders": country.get("borders", [])
    }
    for country in countries if country.get("population", 0) > 10_000_000
]

# Сохранение в JSON
with open("results.json", "w", encoding="utf-8") as f:
    json.dump(filtered_countries, f, indent=4, ensure_ascii=False)

# Подсчёт числа соседей
for country in filtered_countries:
    country["neighbor_count"] = len(country["borders"])

# Топ-3 стран по числу соседей
top_countries = sorted(filtered_countries, key=lambda x: -x["neighbor_count"])[:3]
print("Топ-3 стран по числу соседей:", [country["name"] for country in top_countries])

# Скачивание флагов
for country in top_countries:
    flag_url = country["flags"]["png"]
    flag_response = requests.get(flag_url)
    with open(f"{country['name']}_flag.png", "wb") as f:
        f.write(flag_response.content)


