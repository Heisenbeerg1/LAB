# Подсчёт слов в текстовом файле
input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as infile:
    lines = infile.readlines()

# Общий подсчёт слов
total_words = sum(len(line.split()) for line in lines)

# Вычисление процента слов в каждой строке
results = []
for line in lines:
    word_count = len(line.split())
    percentage = (word_count / total_words * 100) if total_words > 0 else 0
    results.append(f"Строка: {line.strip()} - {percentage:.2f}%\n")

# Запись результата в файл
with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.writelines(results)

print(f"Результаты сохранены в файл {output_file}.")
