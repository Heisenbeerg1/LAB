import requests
from bs4 import BeautifulSoup
import csv

# Константы
base_url = "https://worldathletics.org/records/toplists"
disciplines = ["800m", "1500m", "5000m", "10000m"]
years = range(2001, 2025)
genders = {"men": "M", "women": "W"}

# Сбор данных
results = []

for discipline in disciplines:
    for year in years:
        for gender, gender_code in genders.items():
            url = f"{base_url}/{discipline}/{gender_code}/{year}"
            response = requests.get(url)
            soup = BeautifulSoup(response.content, "html.parser")

            # Анализ HTML и извлечение данных
            try:
                result = soup.find("tr", class_="record-row")
                data = {
                    "year": year,
                    "name": result.find("td", class_="name").text.strip(),
                    "country": result.find("td", class_="country").text.strip(),
                    "time": result.find("td", class_="time").text.strip(),
                    "date": result.find("td", class_="date").text.strip(),
                    "discipline": discipline,
                    "gender": gender
                }
                results.append(data)
            except AttributeError:
                continue

# Сохранение в CSV
with open("top_results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["year", "name", "country", "time", "date", "discipline", "gender"])
    writer.writeheader()
    writer.writerows(results)
