import pickle

# Словарь с данными: страны и население 5 крупнейших городов
countries = {
    "USA": {"New York": 8419600, "Los Angeles": 3980400, "Chicago": 2716000, "Houston": 2328000, "Phoenix": 1690000},
    "India": {"Mumbai": 12442373, "Delhi": 11034555, "Bangalore": 8436675, "Hyderabad": 6809970, "Ahmedabad": 5577940},
    "China": {"Shanghai": 24183300, "Beijing": 21516000, "Chongqing": 15872000, "Tianjin": 13215000, "Guangzhou": 11032000},
    "Germany": {"Berlin": 3769000, "Hamburg": 1841000, "Munich": 1472000, "Cologne": 1086000, "Frankfurt": 753056},
    "Brazil": {"São Paulo": 12252000, "Rio de Janeiro": 6748000, "Brasilia": 3055149, "Salvador": 2886698, "Fortaleza": 2686612},
    "Russia": {"Moscow": 12615279, "Saint Petersburg": 5384342, "Novosibirsk": 1625600, "Yekaterinburg": 1493749, "Kazan": 1257391},
    "Australia": {"Sydney": 5312163, "Melbourne": 5078193, "Brisbane": 2462637, "Perth": 2059484, "Adelaide": 1345777}
}

# Вывод стран и среднего населения
print("Среднее население крупнейших городов по странам:")
for country, cities in countries.items():
    avg_population = sum(cities.values()) / len(cities)
    print(f"{country}: {avg_population:.2f}")

# Страны с максимальным и минимальным средним населением
avg_populations = {country: sum(cities.values()) / len(cities) for country, cities in countries.items()}
max_country = max(avg_populations, key=avg_populations.get)
min_country = min(avg_populations, key=avg_populations.get)
print(f"\nСтрана с максимальным средним населением: {max_country}")
print(f"Страна с минимальным средним населением: {min_country}")

# Города с населением менее 500000
print("\nГорода с населением менее 500000:")
for country, cities in countries.items():
    small_cities = {city: pop for city, pop in cities.items() if pop < 500000}
    if small_cities:
        print(f"{country}: {', '.join(small_cities.keys())}")

# Топ-3 города с наибольшим населением
all_cities = [(city, pop) for country, cities in countries.items() for city, pop in cities.items()]
top_cities = sorted(all_cities, key=lambda x: -x[1])[:3]
print("\nТоп-3 города с наибольшим населением:")
for city, population in top_cities:
    print(f"{city}: {population}")

# Сохранение словаря в бинарный файл
with open("data.pickle", "wb") as f:
    pickle.dump(countries, f)

# Чтение данных из бинарного файла
with open("data.pickle", "rb") as f:
    loaded_data = pickle.load(f)

print("\nДанные из файла data.pickle:")
print(loaded_data)
